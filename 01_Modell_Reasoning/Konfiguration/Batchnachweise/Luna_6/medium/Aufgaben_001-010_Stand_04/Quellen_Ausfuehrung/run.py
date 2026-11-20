#!/usr/bin/env python3
"""Separate, auditable V2 runner. Official evaluator is imported without changes.

Configurable no-model-deadline runner. --tasks/--next, --batch and --setup
select explicit trials. Prior model results are never supplied to agents.
"""
from __future__ import annotations

import argparse
import ast
import asyncio
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import shutil
import shlex
import tempfile
import time
import uuid
import fcntl

from runner_helpers import select_tasks, review_test_evidence

from agentcompass.benchmarks.swebench_pro_verified.swebench_pro_verified import (
    SWEBenchProVerifiedBenchmark, SWEBenchProVerifiedBenchmarkPlan)
from agentcompass.environments.docker import DockerSession, _run_subprocess
from agentcompass.harnesses.codex import CodexHarness
from agentcompass.harnesses.codex_roles_b import instructions as original_instructions

SOURCE_DIR = Path(__file__).resolve().parent
LAB = SOURCE_DIR
HERE = LAB / "experiment-luna-01"
DATA = LAB / "data/swe_bench_pro_verified"
UPSTREAM = LAB / "AgentCompass/src/agentcompass"
BINARY = (Path.home() / ".npm-global/lib/node_modules/@openai/codex/node_modules/"
          "@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex")
AUTH = Path.home() / ".codex/auth.json"
BENCHMARK = SWEBenchProVerifiedBenchmark()
PLAN = SWEBenchProVerifiedBenchmarkPlan(
    scripts_dir=str(DATA / "run_scripts"), dockerfiles_dir=str(DATA / "dockerfiles"))
CONTROL_PATCH = ("diff --git a/.swebench-v2-control-marker.txt b/.swebench-v2-control-marker.txt\n"
                 "new file mode 100644\n--- /dev/null\n+++ b/.swebench-v2-control-marker.txt\n"
                 "@@ -0,0 +1 @@\n+Nonfunctional evaluator control; repository code unchanged.\n")
ALLOWLIST = {"network_mode": "allowlist", "allowed_hosts": [
    {"host": "chatgpt.com", "port": 443}, {"host": "auth.openai.com", "port": 443}], "denied_hosts": []}
SECRET_VALUES: set[str] = set()
RUN_MODEL = "gpt-6-luna"
RUN_REASONING = "medium"


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def learn_secrets(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if any(part in key.lower() for part in ("token", "key", "secret")) and isinstance(item, str):
                if len(item) >= 12:
                    SECRET_VALUES.add(item)
            learn_secrets(item)
    elif isinstance(value, list):
        for item in value:
            learn_secrets(item)


def redact(text):
    text = str(text)
    for secret in sorted(SECRET_VALUES, key=len, reverse=True):
        text = text.replace(secret, "<redacted>")
    text = re.sub(r"(https?://agentcompass:)[^@\s]+@", r"\1<redacted>@", text)
    return text


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not isinstance(value, str):
        value = json.dumps(value, indent=2, ensure_ascii=False, default=str) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(redact(value))
    temporary.replace(path)


async def host(argv, *, timeout=120, check=True):
    result = await _run_subprocess(list(map(str, argv)), timeout=timeout)
    if check and result.returncode:
        raise RuntimeError(redact(f"{argv[0]} failed ({result.returncode}): {result.stderr[-1500:]}"))
    return result


class LoggedSession(DockerSession):
    def __init__(self, container_id, log):
        super().__init__(container_id, workdir="/app")
        self.log = Path(log)
        self.sequence = 0

    async def exec(self, command, **kwargs):
        self.sequence += 1
        started = time.monotonic()
        result = await super().exec(command, **kwargs)
        record = {"sequence": self.sequence, "at": now(), "command": command,
                  "cwd": kwargs.get("cwd"), "elapsed_seconds": time.monotonic() - started,
                  "exit_code": result.returncode, "timed_out": result.timed_out,
                  "stdout": result.stdout, "stderr": result.stderr}
        # cat of the refreshed credential is used by custody only, never archived.
        if isinstance(command, list) and command == ["cat", "/opt/v2-codex/auth.json"]:
            record["stdout"] = "<credential omitted>"
        with self.log.open("a") as output:
            output.write(redact(json.dumps(record, default=str)) + "\n")
        return result

    async def checked(self, command, **kwargs):
        result = await self.exec(command, **kwargs)
        if result.returncode or result.timed_out:
            raise RuntimeError(redact(f"Container preparation failed: {command[0]} "
                                      f"({result.returncode}): {result.stderr[-1500:]}"))
        return result


@asynccontextmanager
async def container(image, directory, *, agent=False):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    suffix = uuid.uuid4().hex[:12]
    name = f"swe-v2-{suffix}"
    network, proxy, cid = None, None, None
    policy_dir = None
    try:
        args = ["docker", "run", "-d", "--name", name, "--cap-drop", "ALL",
                "--cap-add", "CHOWN", "--cap-add", "DAC_OVERRIDE", "--cap-add", "FOWNER",
                "--security-opt", "no-new-privileges", "--pids-limit", "512",
                "--cpus", "4", "--memory", "8192m", "--workdir", "/app",
                "--entrypoint", "/bin/sh"]
        if agent:
            network = name + "-net"
            proxy = name + "-proxy"
            await host(["docker", "network", "create", "--internal", network])
            policy_dir = Path(tempfile.mkdtemp(prefix="swe-v2-policy-"))
            policy_dir.chmod(0o755)
            (policy_dir / "policy.json").write_text(json.dumps(ALLOWLIST))
            token = secrets.token_urlsafe(24)
            SECRET_VALUES.add(token)
            await host(["docker", "run", "-d", "--name", proxy, "--read-only",
                        "--user", "65534:65534", "--cap-drop", "ALL",
                        "--security-opt", "no-new-privileges", "--memory", "128m",
                        "--pids-limit", "64", "-e", "PYTHONDONTWRITEBYTECODE=1",
                        "-e", f"AGENTCOMPASS_PROXY_TOKEN={token}",
                        "-e", "AGENTCOMPASS_POLICY_PATH=/opt/policy/policy.json",
                        "-v", f"{policy_dir}:/opt/policy:ro",
                        "-v", f"{UPSTREAM}/environments/docker_egress_proxy.py:/opt/upstream_proxy.py:ro",
                        "-v", f"{SOURCE_DIR}/egress_proxy.py:/opt/proxy.py:ro",
                        "python:3.12-alpine", "python", "/opt/proxy.py"])
            await host(["docker", "network", "connect", network, proxy])
            proxy_url = f"http://agentcompass:{token}@{proxy}:8080"
            args.extend(["--network", network, "--dns", "127.0.0.1",
                         "--mount", f"type=bind,source={BINARY},target=/usr/local/bin/codex,readonly",
                         "--mount", f"type=bind,source={BINARY.parent}/codex-code-mode-host,target=/usr/local/bin/codex-code-mode-host,readonly",
                         "--mount", f"type=bind,source={SOURCE_DIR}/requirements.toml,target=/etc/codex/requirements.toml,readonly"])
            for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
                args.extend(["-e", f"{key}={proxy_url}"])
            for key, value in {"NO_PROXY": "localhost,127.0.0.1,::1", "no_proxy": "localhost,127.0.0.1,::1",
                               "GOPROXY": "off", "GOSUMDB": "off"}.items():
                args.extend(["-e", f"{key}={value}"])
        else:
            args.extend(["--network", "none"])
        args.extend([image, "-c", "exec tail -f /dev/null"])
        cid = (await host(args)).stdout.strip()
        env = LoggedSession(cid, directory / "commands.jsonl")
        inspect = json.loads((await host(["docker", "inspect", cid])).stdout)[0]
        save(directory / "container.json", {"image": inspect["Image"],
             "networks": list(inspect["NetworkSettings"]["Networks"]),
             "cap_drop": inspect["HostConfig"]["CapDrop"],
             "cap_add": inspect["HostConfig"]["CapAdd"],
             "security_opt": inspect["HostConfig"]["SecurityOpt"],
             "mounts": [{"destination": x["Destination"], "writable": x["RW"]} for x in inspect["Mounts"]]})
        if agent:
            for _ in range(40):
                ready = await host(["docker", "exec", proxy, "python", "-c",
                                    "import socket;socket.create_connection(('127.0.0.1',8080),1).close()"], check=False)
                if ready.returncode == 0:
                    break
                await asyncio.sleep(0.25)
            else:
                raise RuntimeError("Network proxy did not become ready")
        yield env
    finally:
        if proxy:
            logs = await host(["docker", "logs", proxy], check=False)
            save(directory / "network.jsonl", logs.stdout + logs.stderr)
        if cid:
            await host(["docker", "rm", "-f", cid], check=False)
        if proxy:
            await host(["docker", "rm", "-f", proxy], check=False)
        if network:
            await host(["docker", "network", "rm", network], check=False)
        if policy_dir:
            shutil.rmtree(policy_dir, ignore_errors=True)


async def evaluate(instance, image, patch, directory):
    async with container(image, directory) as env:
        started = time.monotonic()
        result = await BENCHMARK._evaluate_patch(env, instance, PLAN, patch, 3600)
        result["elapsed_seconds"] = time.monotonic() - started
        save(Path(directory) / "evaluation.json", result)
        return result


async def verify_toolchain(env, language):
    commands = {
        "go": "command -v go; go version; command -v gofmt",
        "python": "command -v python; python --version; python -c 'import pytest; print(pytest.__version__)'",
        "js": "command -v node; node --version; if command -v yarn >/dev/null; then yarn --version; elif command -v npm >/dev/null; then npm --version; elif command -v pnpm >/dev/null; then pnpm --version; else exit 1; fi",
    }
    if language not in commands:
        raise RuntimeError(f"No validated environment profile for language {language}")
    result = await env.checked(["/bin/bash", "-lc", "set -e; command -v python; python --version; " + commands[language]])
    return result.stdout


async def prepare_toolchain(env, language):
    if language not in ("go", "python", "js"):
        raise RuntimeError(f"Unsupported language profile: {language}")
    tools = ["python", "python3"]
    tools += {"go": ["go", "gofmt"], "python": ["pytest"], "js": ["node", "npm", "yarn", "pnpm"]}[language]
    paths = {}
    # Capture image-installed tools before the Codex login shell rewrites PATH.
    # No installation or dependency downloads; aliases are common to both setups.
    for tool in tools:
        located = await env.exec(["/bin/sh", "-c", "command -v " + tool])
        if located.returncode == 0 and located.stdout.strip().startswith("/"):
            paths[tool] = located.stdout.strip()
    if "python" not in paths and "python3" in paths:
        paths["python"] = paths["python3"]
    for tool, path in paths.items():
        alias = "/usr/bin/" + tool
        # Do not replace existing /usr/bin symlink targets with themselves.
        target = (await env.checked(["readlink", "-f", path])).stdout.strip()
        if path != alias and target != alias:
            await env.checked(["ln", "-sf", path, alias])
    return {"language": language, "image_tool_paths": paths}


async def ensure_image(image, directory):
    """Fetch missing official images on the host, then resolve an immutable ID."""
    started = time.monotonic()
    record = {"requested_image": image, "at": now(), "pulled": False, "model_tokens": 0}
    path = Path(directory) / "image-acquisition.json"
    try:
        inspected = await host(["docker", "image", "inspect", image], check=False)
        if inspected.returncode:
            if "no such image" not in inspected.stderr.lower():
                raise RuntimeError(redact(f"docker image inspect failed: {inspected.stderr[-1500:]}"))
            print(f"Downloading missing official Docker image: {image}", flush=True)
            record.update(pull_started_at=now())
            save(path, record)
            await host(["docker", "pull", image], timeout=None)
            record["pulled"] = True
            inspected = await host(["docker", "image", "inspect", image])
        details = json.loads(inspected.stdout)[0]
        record.update(image_id=details["Id"], completed=True, elapsed_seconds=time.monotonic() - started)
        save(path, record)
        return details
    except Exception as error:
        record.update(completed=False, error=redact(str(error)), elapsed_seconds=time.monotonic() - started)
        save(path, record)
        raise


async def prepare(case, directory):
    original_image = "jefzda/sweap-images:" + case["dockerhub_tag"]
    inspected = await ensure_image(original_image, directory)
    original_image_id = inspected["Id"]
    # Pin existing official image; never pull a different tag between paired runs.
    async with container(original_image_id, directory) as env:
        await env.checked(["git", "-c", "core.hooksPath=/dev/null", "reset", "--hard", case["base_commit"]])
        original_tree = (await env.checked(["git", "write-tree"])).stdout.strip()
        tracked = (await env.checked(["git", "ls-files", "--stage"])).stdout
        save(Path(directory) / "canonical-tracked-files.txt", tracked)
        excludes = ""
        if (await env.exec(["test", "-f", "/app/.git/info/exclude"])).returncode == 0:
            excludes = await env.read_text("/app/.git/info/exclude")
        # Copy ONLY a shallow canonical Git database, retaining the entire installed
        # working environment. Reconstructing an index with git add --all can
        # flatten gitlinks or accidentally track previously ignored dependencies.
        await env.checked(["git", "-c", "core.hooksPath=/dev/null", "clone", "--quiet",
                           "--no-local", "--depth", "1", "--single-branch", "--no-tags",
                           "file:///app", "/tmp/v2-canonical-clone"], timeout=180)
        cloned_head = (await env.checked(["git", "-C", "/tmp/v2-canonical-clone", "rev-parse", "HEAD"])).stdout.strip()
        if cloned_head != case["base_commit"]:
            raise RuntimeError("Shallow clone did not preserve the canonical base commit")
        await env.checked(["rm", "-rf", "/app/.git"])
        await env.checked(["find", "/app", "-name", ".git", "-exec", "rm", "-rf", "--", "{}", "+"])
        await env.checked(["mv", "/tmp/v2-canonical-clone/.git", "/app/.git"])
        await env.checked(["rm", "-rf", "/tmp/v2-canonical-clone"])
        await env.checked(["git", "remote", "remove", "origin"])
        await env.checked(["git", "config", "core.hooksPath", "/dev/null"])
        count = (await env.checked(["git", "rev-list", "--all", "--count"])).stdout.strip()
        if count != "1":
            raise RuntimeError("Additional source history remained accessible")
        new_tree = (await env.checked(["git", "write-tree"])).stdout.strip()
        if original_tree != new_tree:
            raise RuntimeError("Prepared tracked source differs from the canonical original tree")
        await env.checked(["mkdir", "-p", "/app/.codex-role-output"])
        await env.write_text("/app/.git/info/exclude", excludes + "\n.codex-role-output/\n")
        toolchains = await prepare_toolchain(env, case["repo_language"])
        login_toolchains = await verify_toolchain(env, case["repo_language"])
        image_id = (await host(["docker", "commit", env.container_id], timeout=300)).stdout.strip()
    snapshot = {"original_image": original_image, "original_image_id": original_image_id,
                "prepared_image_id": image_id, "canonical_tree": original_tree,
                "repo_language": case["repo_language"], "toolchains": toolchains, "login_shell_toolchains": login_toolchains, "at": now()}
    save(Path(directory) / "snapshot.json", snapshot)
    return snapshot


async def network_checks(env, directory):
    # Test both cooperative proxy use and attempts to bypass it, including raw IP.
    script = r'''import json, os, socket, urllib.request
out = {}
for name, url in [('github', 'https://github.com'), ('search', 'https://www.google.com'), ('ip_via_proxy','https://1.1.1.1')]:
    try:
        urllib.request.urlopen(url, timeout=8)
        out[name] = 'UNEXPECTED_ALLOWED'
    except Exception as error:
        out[name] = str(error)
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
try:
    opener.open('https://github.com', timeout=5)
    out['without_proxy'] = 'UNEXPECTED_ALLOWED'
except Exception as error:
    out['without_proxy'] = str(error)
try:
    socket.create_connection(('1.1.1.1',443), timeout=3).close()
    out['direct_ip'] = 'UNEXPECTED_ALLOWED'
except Exception as error:
    out['direct_ip'] = str(error)
try:
    response = urllib.request.urlopen('https://chatgpt.com', timeout=15)
    out['model_host'] = response.status
except urllib.error.HTTPError as error:
    out['model_host'] = error.code
except Exception as error:
    out['model_host'] = str(error)
print(json.dumps(out))
'''
    result = await env.checked(["python", "-c", script], timeout=90)
    checks = json.loads(result.stdout)
    save(Path(directory) / "network-checks.json", checks)
    if any(value == "UNEXPECTED_ALLOWED" for value in checks.values()):
        raise RuntimeError("An external research route unexpectedly worked")
    if not isinstance(checks["model_host"], int):
        raise RuntimeError("Allowed model host could not be reached")


def role_instructions(role):
    common = ("External research is technically blocked. Use local repository code and existing tests only. "
              "Do not request downloads or delegate. Do not read credentials, private process files, "
              "benchmark solutions or evaluator artifacts. Write/update .codex-role-output/checkpoint.md "
              "early. Never change git history, the index baseline, or harness configuration. ")
    if role == "standard":
        return common + "Resolve the issue by editing the repository and run relevant existing tests."
    text = original_instructions(role)
    if role == "review":
        text = text.replace("Run existing local tests when feasible.",
                            "You MUST attempt relevant existing local tests and report the exact commands and results.")
        text = text.replace("Choose FIX only for a concrete correctness or regression issue;",
                            "Choose FIX for a correctness/regression issue OR any failed, unavailable, interrupted, "
                            "or unexecutable relevant test. ACCEPT requires relevant tests successfully executed. "
                            "Separate code defects from TEST_ENVIRONMENT_PROBLEM; never claim tests passed without execution;")
    if role == "correction":
        text += (" Rerun the exact tests flagged by the reviewer after fixing. No new downloads. "
                 "Report remaining failures and use TEST_ENVIRONMENT_PROBLEM for missing prepared dependencies.")
    return common + text


async def valid_patch(image, patch, directory):
    async with container(image, directory) as env:
        if patch:
            await env.write_text("/tmp/candidate.patch", patch)
            result = await env.exec(["git", "apply", "--check", "--binary", "/tmp/candidate.patch"])
            return result.returncode == 0
        return True


async def model_stage(image, role, prompt, patch, directory, credential):
    directory = Path(directory)
    developer = role_instructions(role)
    save(directory / "prompt.txt", prompt)
    save(directory / "developer-instructions.txt", developer)
    async with container(image, directory, agent=True) as env:
        await network_checks(env, directory)
        await verify_toolchain(env, IMAGE_LANGUAGES[image])
        if patch:
            await env.write_text("/tmp/handoff.patch", patch)
            await env.checked(["git", "apply", "--binary", "/tmp/handoff.patch"])
            await env.checked(["rm", "-f", "/tmp/handoff.patch"])
        await env.checked(["test", "-x", "/usr/local/bin/codex-code-mode-host"])
        await env.checked(["mkdir", "-p", "/opt/v2-codex"])
        await env.upload(str(credential), "/opt/v2-codex/auth.json")
        await env.checked(["chmod", "600", "/opt/v2-codex/auth.json"])
        runtime_env = {"CODEX_HOME": "/opt/v2-codex", "OPENAI_API_KEY": "", "CODEX_API_KEY": "",
                       "AZURE_OPENAI_API_KEY": "", "ANTHROPIC_API_KEY": "", "OPENAI_BASE_URL": ""}
        login = await env.checked(["codex", "login", "status"], required_env=runtime_env)
        if "Logged in using ChatGPT" not in login.stdout + login.stderr:
            raise RuntimeError("Subscription authentication was not verified")
        argv = ["codex", "exec", "--json",
                "--ephemeral", "--ignore-user-config", "--cd", "/app", "--model", RUN_MODEL,
                "--dangerously-bypass-approvals-and-sandbox", "-c", 'forced_login_method="chatgpt"',
                "-c", 'web_search="disabled"', "-c", "model_reasoning_effort=" + json.dumps(RUN_REASONING),
                "-c", "agents.enabled=false", "-c", "features.multi_agent=false",
                "-c", "features.apps=false", "-c", "features.remote_plugin=false",
                "-c", "developer_instructions=" + json.dumps(developer), "--", prompt]
        save(directory / "invocation.json", {"argv": argv, "auth_mode": "chatgpt",
                                             "timeout_seconds": None})
        docker_argv = ["docker", "exec", "-w", "/app"]
        for key, value in runtime_env.items():
            docker_argv.extend(["-e", f"{key}={value}"])
        docker_argv.extend([env.container_id, *argv])
        started = time.monotonic()
        process = await asyncio.create_subprocess_exec(*docker_argv, stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE, limit=64 * 1024 * 1024)
        async def stream(reader, path):
            # Persist events immediately on the trusted host; no log mount in the agent container.
            with path.open("w") as output:
                while True:
                    line = await reader.readline()
                    if not line:
                        break
                    output.write(redact(line.decode(errors="replace")))
                    output.flush()
        streams = asyncio.gather(stream(process.stdout, directory / "events.jsonl"),
                                 stream(process.stderr, directory / "stderr.log"))
        await process.wait()
        await streams
        elapsed = time.monotonic() - started
        refreshed = await env.read_text("/opt/v2-codex/auth.json")
        parsed_auth = json.loads(refreshed)
        learn_secrets(parsed_auth)
        credential.write_text(refreshed)
        # A refresh can create a new secret during execution; scrub retained logs
        # again now that custody knows its values.
        for log_path in directory.glob("*"):
            if log_path.is_file() and log_path.suffix in (".jsonl", ".log"):
                save(log_path, redact(log_path.read_text()))
        events = CodexHarness._parse_json_events((directory / "events.jsonl").read_text())
        reported_errors = [event for event in events if event.get("type") in ("error", "turn.failed")]
        save(directory / "reported-errors.json", reported_errors)
        final = CodexHarness._extract_final_answer(events, "")
        checkpoint = ""
        if (await env.exec(["test", "-f", "/app/.codex-role-output/checkpoint.md"])).returncode == 0:
            checkpoint = await env.read_text("/app/.codex-role-output/checkpoint.md")
        save(directory / "checkpoint.md", checkpoint)
        save(directory / "answer.md", final)
        await env.checked(["git", "add", "-N", "--", "."])
        diff = (await env.checked(["git", "diff", "--binary", BASE_COMMITS[image], "--", ".",
                                   ":(exclude).codex-role-output"])).stdout
        # Diagnosis/review edits are never forwarded, but recorded for audit.
        save(directory / "repository.patch", diff)
        usage = {key: 0 for key in ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens")}
        completed = False
        for event in events:
            if event.get("type") == "turn.completed":
                completed = True
                for key in usage:
                    usage[key] += int((event.get("usage") or {}).get(key) or 0)
        unexpected_tools = [event for event in events if "web_search" in str(event.get("item", {}).get("type", ""))]
        metadata = {"role": role, "elapsed_seconds": elapsed, "exit_code": process.returncode,
                    "timed_out": False, "timeout_seconds": None,
                    "reported_error_count": len(reported_errors), "usage": usage if completed else None,
                    "usage_complete": completed and process.returncode == 0, "handoff": (final or checkpoint)[:6000],
                    "patch_bytes": len(diff.encode()), "unexpected_web_tools": len(unexpected_tools)}
        if role == "review":
            metadata["test_evidence"] = review_test_evidence(events)
        save(directory / "stage.json", metadata)
        if not completed or process.returncode != 0:
            save(directory.parent / "result.json", {
                "setup": "standard" if role == "standard" else "roles-b", "model": RUN_MODEL,
                "auth_mode": "chatgpt", "status": "technical_interruption", "resolved": None,
                "interrupted_role": role, "stages": [metadata],
                "elapsed_codex_seconds": elapsed, "reported_errors": reported_errors,
                "note": "Not a demonstrated functional failure. No automatic retry. Other role logs remain preserved."})
            raise RuntimeError("Technical model interruption; batch paused; inspect preserved logs before a new attempt")
        if CodexHarness._first_error_event(events) is not None or re.search(
                r"failed to spawn .*host", (directory / "stderr.log").read_text()):
            raise RuntimeError("Native Codex/tool startup error; trial is a harness problem, not a solution failure")
        if not completed and not metadata["timed_out"]:
            raise RuntimeError("Codex returned no completed turn; inspect native events before continuing")
        if unexpected_tools:
            raise RuntimeError("A prohibited web tool appeared in the event log")
        if process.returncode not in (0, 124, 137):
            raise RuntimeError(f"Codex stage {role} failed (exit {process.returncode}); see saved logs")
        return metadata, diff if role in ("standard", "implementation", "correction") else ""


def issue_prompt(instance):
    return ("Resolve the issue in the repository at /app. Edit checked-out files; the coordinator exports changes.\n\n"
            "ISSUE:\n" + instance["problem_statement"] + "\n\nREQUIREMENTS:\n" + str(instance.get("requirements", ""))
            + "\n\nINTERFACES:\n" + str(instance.get("interface", "")))


async def trial(instance, image, setup, directory, credential):
    directory = Path(directory)
    stages = []
    issue = issue_prompt(instance)
    correction_started = False
    if setup == "standard":
        stage, patch = await model_stage(image, "standard", issue, "", directory / "standard", credential)
        stages.append(stage)
    else:
        diagnosis, _ = await model_stage(image, "diagnosis", issue, "", directory / "diagnosis", credential)
        stages.append(diagnosis)
        implementation, patch = await model_stage(image, "implementation",
            issue + "\n\nDIAGNOSIS (hypothesis only):\n" + diagnosis["handoff"], "",
            directory / "implementation", credential)
        stages.append(implementation)
        if not await valid_patch(image, patch, directory / "implementation-patch-check"):
            save(directory / "result.json", {"status": "invalid_submission", "stages": stages})
            return
        review, _ = await model_stage(image, "review", issue +
            "\n\nIndependently review the already-applied patch. Run relevant existing tests.\n",
            patch, directory / "review", credential)
        stages.append(review)
        claimed_accept = bool(re.match(r"\s*VERDICT:\s*ACCEPT\b", review["handoff"], re.I))
        accepted = claimed_accept and review["test_evidence"]["accept_supported"]
        review["effective_verdict"] = "ACCEPT" if accepted and not review["timed_out"] else "FIX"
        review["verdict_overridden_for_missing_test_evidence"] = claimed_accept and not accepted
        save(directory / "review/stage.json", review)
        if not accepted or review["timed_out"]:
            correction_started = True
            correction, candidate = await model_stage(image, "correction",
                issue + "\n\nREVIEW:\n" + review["handoff"] +
                ("\n\nCoordinator: effective VERDICT: FIX. The event log did not establish successful "
                 "execution of relevant existing tests; verify and rerun them." if claimed_accept and not accepted else ""), patch,
                directory / "correction", credential)
            stages.append(correction)
            if await valid_patch(image, candidate, directory / "correction-patch-check"):
                patch = candidate
    save(directory / "submission.patch", patch)
    applicable = await valid_patch(image, patch, directory / "final-patch-check")
    result = {"setup": setup, "model": RUN_MODEL, "auth_mode": "chatgpt",
              "stages": stages, "correction_started": correction_started, "patch_applicable": applicable,
              "elapsed_codex_seconds": sum(x["elapsed_seconds"] for x in stages)}
    problem_markers = [match.group(1).strip().lower() for stage in stages for match in
                       re.finditer(r"TEST_ENVIRONMENT_PROBLEM\s*:\s*([^\n]*)", stage["handoff"])]
    result["test_environment_problem_reported"] = any(
        not re.match(r"(?:none|no(?:ne)?\b|not observed)\b", marker) for marker in problem_markers)
    if not applicable:
        result["status"] = "invalid_submission"
    elif not patch.strip():
        result["status"] = "empty_submission"
        result["resolved"] = False
    else:
        evaluation = await evaluate(instance, image=ORIGINAL_IMAGES[instance["instance_id"]], patch=patch,
                                    directory=directory / "evaluation")
        result.update(status="completed" if evaluation.get("completed") and not evaluation.get("error")
                      else "evaluation_problem", resolved=evaluation.get("resolved", False))
    save(directory / "result.json", result)


IMAGE_LANGUAGES = {}
ORIGINAL_IMAGES = {}
BASE_COMMITS = {}








async def parallel_trials(jobs, manifest, manifest_path, credential_root, credential_bytes):
    """Start every selected trial; one technical failure does not cancel siblings."""
    manifest["active_trials"] = []
    manifest["technical_errors"] = []

    async def worker(number, case, setup, directory, instance, image):
        identity = {"task": number, "setup": setup}
        credential = credential_root / f"task-{number:02d}-{setup}-auth.json"
        credential.write_bytes(credential_bytes)
        credential.chmod(0o600)
        save(directory / "started.json", {"at": now(), **identity, "execution_mode": "parallel"})
        manifest["active_trials"].append(identity)
        save(manifest_path, manifest)
        print(f"Task {number}: starting {setup}, {RUN_MODEL} / subscription (parallel)", flush=True)
        try:
            await trial(instance, image, setup, directory, credential)
            result_path = directory / "result.json"
            if result_path.exists() and json.loads(result_path.read_text()).get("status") in ("technical_interruption", "evaluation_problem"):
                raise RuntimeError("Trial reported a technical interruption or evaluation problem; see saved result")
        except Exception as error:
            failure = {**identity, "error": redact(str(error)), "interrupted_at": now()}
            manifest["technical_errors"].append(failure)
            save(directory / "technical-interruption.json", failure)
            print(f"Task {number}: {setup} technical interruption; other trials continue", flush=True)
        else:
            print(f"Task {number}: {setup} complete", flush=True)
        finally:
            manifest["active_trials"].remove(identity)
            save(manifest_path, manifest)

    # Also wait for siblings when an exception occurs before/after trial().
    outcomes = await asyncio.gather(*(worker(*job) for job in jobs), return_exceptions=True)
    for job, outcome in zip(jobs, outcomes):
        if isinstance(outcome, Exception):
            manifest["technical_errors"].append({"task": job[0], "setup": job[2],
                "error": redact(str(outcome)), "interrupted_at": now()})
        elif isinstance(outcome, BaseException):
            raise outcome
    manifest["active_trials"] = []
    if manifest["technical_errors"]:
        manifest.update(status="technical_interruption", interrupted_at=now())
        save(manifest_path, manifest)
        return 2
    return 0


async def ensure_evaluation_scripts(task_numbers, selection):
    """Materialize both official evaluator files before recording their hashes."""
    plan = SWEBenchProVerifiedBenchmarkPlan(scripts_dir=str(DATA / "run_scripts"))
    for number in task_numbers:
        instance_id = selection["scored_tasks"][number - 1]["instance_id"]
        for name in ("run_script.sh", "parser.py"):
            path = DATA / "run_scripts" / instance_id / name
            if not path.is_file():
                print(f"Task {number}: downloading official evaluator file {name}", flush=True)
            await asyncio.to_thread(BENCHMARK._load_local_script, plan, instance_id, name)
            if not path.is_file() or not path.stat().st_size:
                raise RuntimeError(f"Official evaluator file missing or empty: {path}")


async def main(run_models, task_numbers, batch, setup="both", parallel=False, model="gpt-6-luna", reasoning="medium"):
    global RUN_MODEL, RUN_REASONING
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", model):
        raise ValueError("Use a native Codex model ID, for example gpt-6-luna")
    if reasoning not in ("low", "medium", "high", "xhigh", "max"):
        raise ValueError("Unsupported reasoning level")
    RUN_MODEL, RUN_REASONING = model, reasoning
    selection = json.loads((LAB / "selection.json").read_text())
    if sha(DATA / "swebench_pro_verified.jsonl") != selection["dataset_sha256"]:
        raise RuntimeError("Preregistered dataset hash mismatch")
    setups = ["standard", "roles-b"] if setup == "both" else [setup]
    root = HERE / batch
    root.mkdir(exist_ok=True, mode=0o700)
    manifest_path = root / "manifest.json"
    if manifest_path.exists():
        recorded = json.loads(manifest_path.read_text())
        if recorded["status"] in ("completed", "technical_interruption"):
            if recorded["tasks"] != task_numbers or recorded["setups"] != setups:
                raise RuntimeError("Batch task/setup selection differs; use a separate batch")
            if recorded["model"] != model or recorded["reasoning"] != reasoning:
                raise RuntimeError("Batch model/reasoning differs; use a separate batch")
            # No execution occurs: newer central sources cannot rewrite historical runs.
            print(f"Batch already {recorded['status']}; no implicit repeats", flush=True)
            return 0 if recorded["status"] == "completed" else 2
    await ensure_evaluation_scripts(task_numbers, selection)
    source_hashes = {str(path.relative_to(LAB)): sha(path) for path in
        (SOURCE_DIR / "run.py", SOURCE_DIR / "runner_helpers.py", SOURCE_DIR / "report.py", SOURCE_DIR / "egress_proxy.py", SOURCE_DIR / "requirements.toml", LAB / "selection.json",
         UPSTREAM / "benchmarks/swebench_pro_verified/swebench_pro_verified.py",
         UPSTREAM / "harnesses/codex.py", UPSTREAM / "harnesses/codex_roles_b.py",
         UPSTREAM / "environments/docker.py", UPSTREAM / "environments/docker_egress_proxy.py")}
    if (HERE / "experiment.json").is_file():
        source_hashes[str((HERE / "experiment.json").relative_to(LAB))] = sha(HERE / "experiment.json")
    for number in task_numbers:
        instance_id = selection["scored_tasks"][number - 1]["instance_id"]
        for path in sorted((DATA / "run_scripts" / instance_id).rglob("*")):
            if path.is_file():
                source_hashes[str(path.relative_to(LAB))] = sha(path)
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        if manifest["source_hashes"] != source_hashes:
            raise RuntimeError("Versioned sources changed since validation; create a new batch or explicitly invalidate controls")
        if manifest["model"] != model or manifest["reasoning"] != reasoning:
            raise RuntimeError("Batch model/reasoning differs; use a separate batch")
        if manifest.get("execution_source_hashes", source_hashes) != source_hashes:
            raise RuntimeError("Execution sources changed since the first model start; use a new batch")
        requested_mode = "parallel" if parallel else "sequential"
        prior_mode = manifest.get("execution_mode")
        if prior_mode is None and any(root.glob("task-*/*/started.json")):
            prior_mode = "sequential"
        if run_models and prior_mode is not None and prior_mode != requested_mode:
            raise RuntimeError("Execution mode is frozen after the first model start; use a new batch")
        if manifest["tasks"] != task_numbers or manifest["setups"] != setups:
            raise RuntimeError("Batch task/setup selection differs; use a separate batch")
        if manifest["status"] in ("completed", "technical_interruption"):
            print(f"Batch already {manifest['status']}; no implicit repeats", flush=True)
            return 0 if manifest["status"] == "completed" else 2
    else:
        manifest = {"version": "harness-v6-central-runner", "created_at": now(), "status": "validating",
                    "tasks": task_numbers, "setups": setups, "model": RUN_MODEL,
                    "model_timeout_seconds": None, "evaluation_timeout_seconds": 3600,
                    "reasoning": RUN_REASONING, "auth_mode": "chatgpt", "source_hashes": source_hashes,
                    "network_policy": ALLOWLIST, "control_marker_patch_sha256": hashlib.sha256(CONTROL_PATCH.encode()).hexdigest()}
        save(manifest_path, manifest)
        for key in source_hashes:
            source = LAB / key
            destination = root / "source-snapshot" / key
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    cases = [(number, selection["scored_tasks"][number - 1]) for number in task_numbers]
    wanted = {case["instance_id"] for _, case in cases}
    instances = {}
    with (DATA / "swebench_pro_verified.jsonl").open() as dataset:
        for line in dataset:
            item = json.loads(line)
            if item["instance_id"] in wanted:
                instances[item["instance_id"]] = item
    # Reference solutions stay in host memory and trusted control containers only.
    snapshots = {}
    for number, case in cases:
        task_dir = root / f"task-{number:02d}"
        controls_path = task_dir / "controls.json"
        if controls_path.exists():
            controls = json.loads(controls_path.read_text())
            if not controls["passed"]:
                raise RuntimeError(f"Task {number} previously failed controls; inspect before proceeding")
            snapshots[number] = json.loads((task_dir / "preparation/snapshot.json").read_text())
        else:
            print(f"Task {number}: preparing identical offline snapshot", flush=True)
            snapshot = await prepare(case, task_dir / "preparation")
            snapshots[number] = snapshot
            instance = instances[case["instance_id"]]
            print(f"Task {number}: running no-model original/reference controls", flush=True)
            base = await evaluate(instance, snapshot["original_image_id"], CONTROL_PATCH, task_dir / "controls-original")
            gold = await evaluate(instance, snapshot["original_image_id"], str(instance["patch"]), task_dir / "controls-reference")
            required_fails = set(BENCHMARK._list_field(instance, "fail_to_pass"))
            base_passed = {test["name"] for test in base.get("tests", []) if test["status"] == "PASSED"}
            passed = bool(base.get("completed") and not base.get("error") and required_fails
                          and required_fails.isdisjoint(base_passed) and not base.get("pass_to_pass_missing")
                          and gold.get("completed") and gold.get("resolved") and not gold.get("error"))
            controls = {"passed": passed, "original_completed": base.get("completed"),
                        "original_resolved": base.get("resolved"), "reference_resolved": gold.get("resolved"),
                        "model_tokens": 0, "at": now()}
            save(controls_path, controls)
            print(f"Task {number}: controls {'PASS' if passed else 'BLOCKED'}", flush=True)
            if not passed:
                manifest.update(status="control_problem", task=number)
                save(manifest_path, manifest)
                return 2
        ORIGINAL_IMAGES[case["instance_id"]] = snapshots[number]["original_image_id"]
        BASE_COMMITS[snapshots[number]["prepared_image_id"]] = case["base_commit"]
        IMAGE_LANGUAGES[snapshots[number]["prepared_image_id"]] = case["repo_language"]
    manifest.update(status="controls_passed", controls_at=now())
    save(manifest_path, manifest)
    if not run_models:
        return 0
    if not AUTH.is_file() or not BINARY.is_file():
        raise RuntimeError("Subscription credential or native Codex executable missing")
    # Check the entire selection before starting any concurrent model process.
    if parallel:
        for number, case in cases:
            for selected_setup in setups:
                directory = root / f"task-{number:02d}" / selected_setup
                if (directory / "started.json").exists() and not (directory / "result.json").exists():
                    raise RuntimeError("An incomplete previous trial exists; no implicit model retry")
    manifest.update(execution_mode="parallel" if parallel else "sequential",
                    execution_runner_version="harness-v6-central-runner",
                    execution_source_hashes=source_hashes,
                    container_limits={"cpus": 4, "memory_mib": 8192})
    if "execution_started_at" not in manifest:
        manifest["execution_started_at"] = now()
        for key in source_hashes:
            destination = root / "execution-source-snapshot" / key
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(LAB / key, destination)
    save(manifest_path, manifest)
    # Credentials are temporary and outside all archived run directories.
    with tempfile.TemporaryDirectory(prefix="swe-v2-credentials-") as private:
        credential = Path(private) / "auth.json"
        credential.write_bytes(AUTH.read_bytes())
        credential.chmod(0o600)
        learn_secrets(json.loads(credential.read_text()))
        if parallel:
            jobs = [(number, case, selected_setup, root / f"task-{number:02d}" / selected_setup,
                     instances[case["instance_id"]], snapshots[number]["prepared_image_id"])
                    for number, case in cases for selected_setup in setups
                    if not (root / f"task-{number:02d}" / selected_setup / "result.json").exists()]
            manifest.update(status="running")
            save(manifest_path, manifest)
            result = await parallel_trials(jobs, manifest, manifest_path, Path(private), credential.read_bytes())
            if result:
                return result
        else:
            for number, case in cases:
                for setup in setups:
                    directory = root / f"task-{number:02d}" / setup
                    if (directory / "result.json").exists():
                        continue
                    if (directory / "started.json").exists():
                        raise RuntimeError("An incomplete previous trial exists; no implicit model retry")
                    save(directory / "started.json", {"at": now(), "task": number, "setup": setup})
                    manifest.update(status="running", active_task=number, active_setup=setup)
                    save(manifest_path, manifest)
                    print(f"Task {number}: starting {setup}, {RUN_MODEL} / subscription", flush=True)
                    try:
                        await trial(instances[case["instance_id"]], snapshots[number]["prepared_image_id"],
                                    setup, directory, credential)
                    except RuntimeError as error:
                        manifest.update(status="technical_interruption", error=redact(str(error)), interrupted_at=now())
                        save(manifest_path, manifest)
                        raise
                    print(f"Task {number}: {setup} complete", flush=True)
    manifest.update(status="completed", completed_at=now())
    manifest.pop("active_task", None)
    manifest.pop("active_setup", None)
    save(manifest_path, manifest)
    return 0


def experiment_directory(name):
    if not re.fullmatch(r"experiment-[A-Za-z0-9][A-Za-z0-9_-]*", name):
        raise ValueError("Use an experiment directory name such as experiment-luna-01")
    directory = (LAB / name).resolve()
    if directory.parent != LAB.resolve():
        raise ValueError("Experiment must be a direct directory inside the laboratory")
    return directory


def resolve_model_configuration(directory, batch, model=None, reasoning=None):
    config_path = directory / "experiment.json"
    config = json.loads(config_path.read_text()) if config_path.is_file() else {}
    manifest_path = directory / batch / "manifest.json"
    recorded = json.loads(manifest_path.read_text()) if manifest_path.is_file() else {}
    return (model or recorded.get("model") or config.get("model", "gpt-6.1-sol"),
            reasoning or recorded.get("reasoning") or config.get("reasoning", "medium"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subscription benchmark; fixed preregistered selection, no model deadline")
    parser.add_argument("--experiment", required=True, help="Output/selection directory inside the lab, for example experiment-luna-01")
    parser.add_argument("--run", action="store_true", help="Run selected model trials after passing controls; consumes subscription capacity")
    parser.add_argument("--parallel", action="store_true", help="With --run, start all selected task/setup trials concurrently; controls stay sequential")
    parser.add_argument("--batch", help="Separate output directory, for example batch-02")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--tasks", help="Preregistered task numbers, for example 4-6 or 4,5,6")
    group.add_argument("--next", type=int, dest="next_count", help="Reserve next N unassigned tasks; freeze selection in this batch")
    parser.add_argument("--model", help="Native Codex subscription model; existing batch or experiment.json supplies the default")
    parser.add_argument("--reasoning", choices=("low", "medium", "high", "xhigh", "max"))
    parser.add_argument("--setup", choices=("standard", "roles-b", "both"), default="both")
    parser.add_argument("--list", action="store_true", help="List fixed task order without preparation or model calls")
    args = parser.parse_args()
    try:
        HERE = experiment_directory(args.experiment)
    except ValueError as error:
        parser.error(str(error))
    selection = json.loads((LAB / "selection.json").read_text())
    if args.list:
        for number, case in enumerate(selection["scored_tasks"], 1):
            print(f"{number:2d}  {case['repo_language']:6s}  {case['repo']}  {case['instance_id']}")
        raise SystemExit(0)
    if not args.batch or not re.fullmatch(r"batch-[A-Za-z0-9][A-Za-z0-9_-]*", args.batch):
        parser.error("--batch is required and must be a separate name such as batch-02")
    if not args.tasks and not args.next_count:
        parser.error("Specify --tasks 4-6 or --next 3")
    if args.next_count is not None and args.next_count < 1:
        parser.error("--next must be positive")
    HERE.mkdir(exist_ok=True, mode=0o700)
    args.model, args.reasoning = resolve_model_configuration(HERE, args.batch, args.model, args.reasoning)
    with (HERE / ".runner.lock").open("a") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.error("Another coordinator is already running for this batch")
        try:
            numbers = select_tasks(args.tasks, args.next_count, selection, HERE, args.batch)
        except ValueError as error:
            parser.error(str(error))
        print(f"Experiment {HERE.name}; batch {args.batch}: tasks {numbers}, setup {args.setup}, {args.model}/{args.reasoning}, no model deadline", flush=True)
        raise SystemExit(asyncio.run(main(args.run, numbers, args.batch, args.setup, args.parallel, args.model, args.reasoning)))
