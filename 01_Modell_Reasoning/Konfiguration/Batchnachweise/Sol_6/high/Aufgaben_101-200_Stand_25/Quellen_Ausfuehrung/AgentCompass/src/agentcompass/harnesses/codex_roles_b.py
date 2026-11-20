"""Fixed four-role Codex experiment using the local ChatGPT subscription login."""

from __future__ import annotations

import hashlib
import json
import re
import time
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from agentcompass.harnesses.codex import CodexConfig, CodexHarness, CodexHarnessPlan
from agentcompass.harnesses.utils.result import read_recorded_output, recorded_command
from agentcompass.runtime import HARNESSES, EnvironmentSession, ExecResult, PreparedTask, RunRequest, RunResult, TaskStatus
from agentcompass.runtime.config import config_field
from agentcompass.utils.workspace import resolve_task_workspace


CHECKPOINT = ".codex-role-output/checkpoint.md"
ROLES = ("diagnosis", "implementation", "review", "correction")


@dataclass(slots=True)
class RolesBConfig(CodexConfig):
    role_timeout_seconds: int = config_field(default=900, description="Per-role Codex deadline in seconds.")

    def __post_init__(self) -> None:
        super(RolesBConfig, self).__post_init__()
        self.role_timeout_seconds = int(self.role_timeout_seconds)
        if self.auth_mode != "chatgpt":
            raise ValueError("codex_roles_b requires auth_mode=chatgpt")
        if self.role_timeout_seconds <= 0:
            raise ValueError("role_timeout_seconds must be positive")


@dataclass(slots=True)
class RolesBPlan(CodexHarnessPlan):
    role_timeout_seconds: int = 900


def instructions(role: str) -> str:
    common = (
        "You are one specialist in a controlled SWE-bench experiment. Work only inside this "
        "repository. Do not search the web or seek benchmark solutions, reference patches, "
        "hidden tests, prior attempts, or evaluation reports. Do not delegate to other agents. "
        "You have a fresh conversation and may rely only on the task and explicit handoff. "
        f"Write a short progress note in {CHECKPOINT} early and update it as you learn. "
        "This note is excluded from the submitted patch. "
    )
    specific = {
        "diagnosis": (
            "Act as a fault-localization specialist. Inspect code and existing tests; do not "
            "modify project source or tests. Return a concise evidence-based diagnosis with "
            "likely files/functions, uncertainty, and behavior the fix should cover."
        ),
        "implementation": (
            "Act as the implementer. Treat the diagnosis as a hypothesis, verify it against "
            "the repository, implement the issue, and run relevant existing local tests where "
            "feasible. Make a coherent code patch."
        ),
        "review": (
            "Act as an independent reviewer. Inspect the issue, current diff, and relevant "
            "code. Run existing local tests when feasible. Do not write new tests or change "
            "project code. Start both your progress note and final answer with exactly "
            "VERDICT: ACCEPT or VERDICT: FIX. Choose FIX only for a concrete correctness or "
            "regression issue; give paths, evidence, and an actionable correction."
        ),
        "correction": (
            "Act as a fresh implementer for one correction round. Inspect the current patch "
            "and independent review. Fix concrete problems identified by the reviewer, and "
            "run relevant existing local tests where feasible. Keep the final patch coherent."
        ),
    }
    return common + specific[role]


@HARNESSES.register()
class CodexRolesBHarness(CodexHarness):
    id = "codex_roles_b"
    description = "Fixed diagnosis, implementation, review, and optional correction with fresh ChatGPT-authenticated Codex processes."
    config_class = RolesBConfig
    plan_class = RolesBPlan

    async def execute_task(
        self, session: dict[str, Any], prepared: PreparedTask, req: RunRequest, plan: RolesBPlan,
    ) -> RunResult:
        env: EnvironmentSession = session["env"]
        workspace = await resolve_task_workspace(env, prepared.input.workspace)
        issue = str(prepared.input.prompt or "").strip().replace(
            "Produce the minimal unified diff patch that resolves the issue.",
            "Modify the checked-out source files to resolve the issue.",
        ).replace(
            "Write only the final unified diff patch to the requested output file.",
            "The coordinator collects your repository changes after you finish.",
        )
        if not issue:
            raise ValueError("codex_roles_b requires a task prompt")
        patch_path = next((str(spec.path) for spec in prepared.output.files
                           if str(spec.path).endswith("/patch.txt")), "")
        if not patch_path:
            raise ValueError("codex_roles_b requires a patch.txt output")

        private = f"/tmp/agentcompass-roles-b-{uuid.uuid4().hex}"
        credential = f"{private}/credential/auth.json"
        await self._checked(env, ["mkdir", "-p", f"{private}/credential"])
        await env.upload(plan.chatgpt_auth_file, credential)
        await self._checked(env, ["chmod", "600", credential])
        stages: list[dict[str, Any]] = []
        initial_patch = ""
        final_patch = ""
        final_patch_source = "implementation"
        initial_patch_valid = True
        correction_patch_valid: bool | None = None
        correction_started = False
        run_error = ""
        started = time.monotonic()

        async def checkout(role: str, patch: str = "") -> str:
            repo = f"{private}/{role}-repo"
            await self._checked(env, ["git", "clone", "--quiet", "--no-hardlinks", "--depth", "1",
                                      f"file://{workspace}", repo], timeout=180)
            await self._checked(env, ["mkdir", "-p", f"{repo}/.codex-role-output"])
            await env.write_text(f"{repo}/.git/info/exclude", ".codex-role-output/\n")
            if patch:
                patch_file = f"{private}/{role}-input.patch"
                await env.write_text(patch_file, patch)
                await self._checked(env, ["git", "apply", "--binary", patch_file], cwd=repo)
            return repo

        async def handoff(stage: dict[str, Any]) -> str:
            return str(stage.get("handoff") or "No written result was available before this role stopped.")[:6000]

        async def stage(role: str, prompt: str, patch: str = "") -> tuple[dict[str, Any], str]:
            repo = await checkout(role, patch)
            home = f"{private}/{role}-home"
            await self._checked(env, ["mkdir", "-p", home])
            await self._checked(env, ["cp", credential, f"{home}/auth.json"])
            await self._checked(env, ["chmod", "600", f"{home}/auth.json"])
            argv = [session["binary"], "exec", "--json", "--ephemeral", "--ignore-user-config",
                    "--cd", repo, "--model", req.model.id,
                    "--sandbox", str(plan.sandbox),
                    "-c", 'forced_login_method="chatgpt"',
                    "-c", "agents.enabled=false",
                    "-c", "developer_instructions=" + json.dumps(instructions(role))]
            if plan.reasoning_effort:
                argv.extend(["-c", "model_reasoning_effort=" + json.dumps(plan.reasoning_effort)])
            if plan.dangerously_bypass_approvals_and_sandbox:
                argv.append("--dangerously-bypass-approvals-and-sandbox")
            argv.extend(["--", prompt])
            token = uuid.uuid4().hex
            stdout_path = f"{private}/{token}.stdout.jsonl"
            stderr_path = f"{private}/{token}.stderr.log"
            stage_started = time.monotonic()
            command = recorded_command(argv, stdout_path, stderr_path)
            result = await env.exec(command, cwd=repo, timeout=plan.role_timeout_seconds,
                                    required_env={"CODEX_HOME": home, "OPENAI_API_KEY": "",
                                                  "CODEX_API_KEY": "", "AZURE_OPENAI_API_KEY": "",
                                                  "ANTHROPIC_API_KEY": ""},
                                    flags={"polling_exec": True})
            await read_recorded_output(env, result, stdout_path, stderr_path)
            events = self._parse_json_events(result.stdout)
            final_answer = self._extract_final_answer(events, "")
            checkpoint = await self._read_optional(env, f"{repo}/{CHECKPOINT}")
            handoff_text = (final_answer or checkpoint).strip()[:6000]
            usage = {key: 0 for key in ("input_tokens", "cached_input_tokens", "output_tokens",
                                        "reasoning_output_tokens")}
            completed = False
            for event in events:
                if event.get("type") == "turn.completed":
                    completed = True
                    for key in usage:
                        usage[key] += int((event.get("usage") or {}).get(key) or 0)
            # Retain only the refreshed credential. Nothing else from this Codex home
            # or checkout is available to the next specialist.
            await self._checked(env, ["cp", f"{home}/auth.json", credential])
            patch_out = await self._diff(env, repo) if role in {"implementation", "correction"} else ""
            metadata = {
                "role": role, "elapsed_seconds": round(time.monotonic() - stage_started, 2),
                "timeout_seconds": plan.role_timeout_seconds, "timed_out": result.timed_out,
                "exit_code": result.returncode, "usage": usage if completed else None,
                "usage_complete": completed and not result.timed_out and result.returncode == 0,
                "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                "handoff_available": bool(handoff_text), "handoff": handoff_text,
                "patch_bytes": len(patch_out.encode()),
            }
            await self._checked(env, ["rm", "-rf", "--", repo, home, stdout_path, stderr_path])
            stages.append(metadata)
            return metadata, patch_out

        try:
            diagnosis, _ = await stage("diagnosis", "Investigate this issue in the current repository.\n\n" + issue)
            implementation, initial_patch = await stage(
                "implementation", "Resolve this issue in the current repository. The diagnosis "
                "below is a lead, not an unquestionable conclusion.\n\nISSUE:\n" + issue
                + "\n\nDIAGNOSIS:\n" + await handoff(diagnosis))
            initial_patch_valid = await self._patch_valid(env, workspace, private, initial_patch)
            if not initial_patch_valid:
                initial_patch = ""
            review, _ = await stage(
                "review", "Independently review the current repository diff against the issue. "
                "Use only existing local tests. The code patch is already applied. "
                "Do not read other agents' private transcripts.\n\nISSUE:\n" + issue
                + ("\n\nThe implementer's partial patch was invalid after a timeout. "
                   "Review the unfixed base and return FIX." if not initial_patch_valid else ""),
                initial_patch)
            review_text = await handoff(review)
            accept = bool(re.match(r"\s*VERDICT:\s*ACCEPT\b", review_text, re.I))
            correction_started = review["timed_out"] or not accept or not initial_patch_valid
            final_patch = initial_patch
            if correction_started:
                correction, candidate = await stage(
                    "correction", "Perform the single correction round on the already-applied "
                    "patch. If review was unavailable, independently inspect and improve it.\n\n"
                    "ISSUE:\n" + issue + "\n\nREVIEW:\n" + review_text, initial_patch)
                correction_patch_valid = await self._patch_valid(env, workspace, private, candidate)
                if correction_patch_valid:
                    final_patch = candidate
                    final_patch_source = "correction"
                else:
                    final_patch_source = "implementation_fallback"
            await env.write_text(patch_path, final_patch)
            for item in stages:
                if item["exit_code"] != 0 and not item["timed_out"]:
                    run_error = f"Codex {item['role']} exited {item['exit_code']}"
                    break
        finally:
            await env.exec(["rm", "-rf", "--", private])

        return RunResult(
            task_id=prepared.task_id,
            status=TaskStatus.RUN_ERROR if run_error else TaskStatus.COMPLETED,
            final_answer=final_patch,
            telemetry={
                "auth_mode": "chatgpt", "model_base_url": None, "model_api_protocol": None,
                "configuration": "roles-b-fixed-coordinator", "role_timeout_seconds": plan.role_timeout_seconds,
                "stages": stages, "correction_started": correction_started,
                "initial_patch_valid": initial_patch_valid,
                "correction_patch_valid": correction_patch_valid,
                "final_patch_source": final_patch_source,
                "elapsed_codex_seconds": round(sum(s["elapsed_seconds"] for s in stages), 2),
                "elapsed_total_seconds": round(time.monotonic() - started, 2),
                "usage_complete": all(s["usage_complete"] for s in stages),
                "patch_bytes": len(final_patch.encode()), "run_error": run_error,
            },
            artifacts={"file": {patch_path: final_patch}},
        )

    @staticmethod
    async def _checked(env: EnvironmentSession, argv: list[str], **kwargs: Any) -> ExecResult:
        result = await env.exec(argv, **kwargs)
        if result.returncode != 0:
            raise RuntimeError(f"Roles-B setup failed: {argv[0]} {argv[1] if len(argv) > 1 else ''}: "
                               f"{result.stderr.strip()[:500]}")
        return result

    @staticmethod
    async def _read_optional(env: EnvironmentSession, path: str) -> str:
        try:
            return await env.read_text(path)
        except FileNotFoundError:
            return ""

    @classmethod
    async def _diff(cls, env: EnvironmentSession, repo: str) -> str:
        await cls._checked(env, ["git", "add", "-N", "--", "."], cwd=repo)
        result = await cls._checked(env, ["git", "diff", "--binary", "HEAD", "--", ".",
                                          ":(exclude).codex-role-output"], cwd=repo)
        return result.stdout

    @classmethod
    async def _patch_valid(cls, env: EnvironmentSession, workspace: str, private: str,
                           patch: str) -> bool:
        if not patch:
            return True
        path = f"{private}/candidate.patch"
        await env.write_text(path, patch)
        # The original workspace is still at the benchmark's sanitized base commit.
        result = await env.exec(["git", "apply", "--check", "--binary", path], cwd=workspace)
        return result.returncode == 0
