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
    profile = "js" if language == "ts" else language
    commands = {
        "go": "command -v go; go version; command -v gofmt",
        "python": "command -v python; python --version; python -c 'import pytest; print(pytest.__version__)'",
        # npm ships with Node. Do not probe an unused Corepack yarn shim first:
        # merely asking for its version can trigger a blocked registry lookup.
        "js": "command -v node; node --version; if command -v npm >/dev/null; then npm --version; elif command -v yarn >/dev/null; then COREPACK_ENABLE_NETWORK=0 COREPACK_DEFAULT_TO_LATEST=0 yarn --version; elif command -v pnpm >/dev/null; then COREPACK_ENABLE_NETWORK=0 COREPACK_DEFAULT_TO_LATEST=0 pnpm --version; else exit 1; fi",
    }
    if profile not in commands:
        raise RuntimeError(f"No validated environment profile for language {language}")
    result = await env.checked(["/bin/bash", "-lc", "set -e; command -v python; python --version; " + commands[profile]])
    return result.stdout


async def prepare_toolchain(env, language):
    profile = "js" if language == "ts" else language
    if profile not in ("go", "python", "js"):
        raise RuntimeError(f"Unsupported language profile: {language}")
    tools = ["python", "python3"]
    tools += {"go": ["go", "gofmt"], "python": ["pytest"], "js": ["node", "npm", "yarn", "pnpm"]}[profile]
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
    official_image_id = original_image_id
    cache_overrides = DATA / "dependency-cache-overrides.json"
    if cache_overrides.is_file():
        override = json.loads(cache_overrides.read_text()).get(case["instance_id"])
        if override:
            if override["official_image_id"] != official_image_id or override["base_commit"] != case["base_commit"]:
                raise RuntimeError("Dependency cache overlay does not match the pinned official source")
            await host(["docker", "image", "inspect", override["cached_image_id"]])
            original_image_id = override["cached_image_id"]
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
    snapshot = {"original_image": original_image, "official_image_id": official_image_id, "original_image_id": original_image_id,
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








async def parallel_trials(jobs, manifest, manifest_path, credential_root, credential_bytes, workers=None):
    """Bound whole trial pipelines; technical failures do not cancel siblings."""
    if workers is not None and workers < 1:
        raise ValueError("Model workers must be positive")
    semaphore = asyncio.Semaphore(workers or max(1, len(jobs)))
    manifest["active_trials"] = []
    manifest["technical_errors"] = []

    async def active_worker(number, case, setup, directory, instance, image):
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

    async def worker(*job):
        async with semaphore:
            await active_worker(*job)

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


async def validate_task_controls(number, case, instance, root):
    """One isolated preparation/control pipeline; no model or credential access."""
    task_dir = root / f"task-{number:02d}"
    controls_path = task_dir / "controls.json"
    if controls_path.exists():
        controls = json.loads(controls_path.read_text())
        if not controls["passed"]:
            raise RuntimeError(f"Task {number} previously failed controls; inspect before proceeding")
        return json.loads((task_dir / "preparation/snapshot.json").read_text()), True
    print(f"Task {number}: preparing identical offline snapshot", flush=True)
    snapshot = await prepare(case, task_dir / "preparation")
    print(f"Task {number}: running no-model original/reference controls", flush=True)
    # Keep original and reference sequential within a task: at most one control
    # container per worker. Different tasks use different containers/directories.
    base = await evaluate(instance, snapshot["original_image_id"], CONTROL_PATCH, task_dir / "controls-original")
    gold = await evaluate(instance, snapshot["original_image_id"], str(instance["patch"]), task_dir / "controls-reference")
    required_fails = set(BENCHMARK._list_field(instance, "fail_to_pass"))
    base_passed = {test["name"] for test in base.get("tests", []) if test["status"] == "PASSED"}
    passed = bool(base.get("completed") and not base.get("error") and required_fails
                  and required_fails.isdisjoint(base_passed) and not base.get("pass_to_pass_missing")
                  and gold.get("completed") and gold.get("resolved") and not gold.get("error"))
    save(controls_path, {"passed": passed, "original_completed": base.get("completed"),
                        "original_resolved": base.get("resolved"), "reference_resolved": gold.get("resolved"),
                        "model_tokens": 0, "at": now()})
    print(f"Task {number}: controls {'PASS' if passed else 'BLOCKED'}", flush=True)
    return snapshot, passed


async def task_controls(cases, instances, root, manifest, manifest_path, workers=1):
    """Bound control concurrency; wait for siblings and gate every model start."""
    semaphore = asyncio.Semaphore(workers)
    snapshots, failures = {}, []

    async def worker(number, case):
        async with semaphore:
            try:
                snapshot, passed = await validate_task_controls(number, case, instances[case["instance_id"]], root)
                snapshots[number] = snapshot
                if not passed:
                    failures.append({"task": number, "kind": "control_failed"})
            except Exception as error:
                failure = {"task": number, "kind": "technical_interruption", "error": redact(str(error)), "at": now()}
                save(root / f"task-{number:02d}" / "controls-interruption.json", failure)
                failures.append(failure)
                print(f"Task {number}: control technical interruption", flush=True)

    if workers == 1:
        for number, case in cases:
            await worker(number, case)
            if failures:
                break
    else:
        await asyncio.gather(*(worker(number, case) for number, case in cases))
    if failures:
        manifest.update(status="control_problem", control_errors=sorted(failures, key=lambda x: x["task"]))
        save(manifest_path, manifest)
        return None
    return snapshots


def load_selection(directory, requested=None, *, pin=False):
    """New experiment pools are immutable; legacy experiments retain their pool."""
    local = directory / "selection.json"
    source = local if local.is_file() else LAB / "selection.json"
    if requested:
        if not re.fullmatch(r"selection(?:-[A-Za-z0-9_-]+)?\.json", requested):
            raise ValueError("Use a lab selection filename such as selection-extended.json")
        source = (LAB / requested).resolve()
        if source.parent != LAB.resolve():
            raise ValueError("Selection must be inside the laboratory")
        if local.exists() and sha(local) != sha(source):
            raise ValueError("Experiment task pool is frozen; use a new experiment")
        if not local.exists() and any(directory.glob("batch-*/manifest.json")):
            raise ValueError("Existing experiment uses the original task pool; use a new experiment")
    selection = json.loads(source.read_text())
    ids = [case["instance_id"] for case in selection["scored_tasks"]]
    if not ids or len(ids) != len(set(ids)) or selection["smoke_test"]["instance_id"] in ids:
        raise ValueError("Selection must contain unique tasks and exclude the smoke test")
    if requested and pin and not local.exists():
        save(local, selection)
        source = local
    return source, selection


def repair_control_attempt(root, manifest, source_hashes, policy, exclusions=()):
    """Explicit, pre-model repair. Preserve passed controls and archive failures."""
    if manifest["status"] not in ("validating", "control_problem", "controls_passed", "technical_interruption"):
        raise RuntimeError("Control repair is only allowed before model execution")
    if manifest.get("execution_started_at") or any(root.glob("task-*/*/started.json")):
        raise RuntimeError("Model trials already started; control repair requires a separate experiment")
    if not set(exclusions) <= set(manifest["tasks"]):
        raise ValueError("Excluded controls must belong to this batch")
    for number in exclusions:
        path = root / f"task-{number:02d}" / "controls.json"
        if not path.exists() or json.loads(path.read_text()).get("passed"):
            raise RuntimeError("Control repair exclusions require existing failed controls")
    prior = manifest["source_hashes"]
    changed = {k for k in prior.keys() | source_hashes.keys() if prior.get(k) != source_hashes.get(k)}
    cache_key = str((DATA / "dependency-cache-overrides.json").relative_to(LAB))
    if changed - {str((SOURCE_DIR / "run.py").relative_to(LAB)), cache_key}:
        raise RuntimeError("Control repair may only change the runner; dataset, evaluator and other sources must remain frozen")
    old_script = root / "source-snapshot" / str((SOURCE_DIR / "run.py").relative_to(LAB))
    old_ast, new_ast = ast.parse(old_script.read_text()), ast.parse((SOURCE_DIR / "run.py").read_text())
    protected = ("evaluate", "container", "trial", "model_stage", "role_instructions", "issue_prompt",
                 "network_checks", "valid_patch", "validate_task_controls", "task_controls")
    for name in protected:
        def body(tree):
            return next(n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name)
        if ast.dump(body(old_ast)) != ast.dump(body(new_ast)):
            raise RuntimeError(f"Protected control/model behavior changed: {name}")
    if cache_key in changed:
        selection = json.loads((HERE / "selection.json" if (HERE / "selection.json").is_file() else LAB / "selection.json").read_text())
        overrides = json.loads((DATA / "dependency-cache-overrides.json").read_text())
        for n in manifest["tasks"]:
            p = root / f"task-{n:02d}" / "controls.json"
            override = overrides.get(selection["scored_tasks"][n - 1]["instance_id"])
            if p.exists() and json.loads(p.read_text()).get("passed") and override:
                snapshot = json.loads((p.parent / "preparation/snapshot.json").read_text())
                if snapshot["original_image_id"] != override["cached_image_id"]:
                    raise RuntimeError("A passing control would receive a different dependency image; use a new batch")
    archive = root / "technical-interruptions" / ("control-repair-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:6])
    archive.mkdir(parents=True)
    shutil.copy2(root / "manifest.json", archive / "manifest.json")
    shutil.move(str(root / "source-snapshot"), str(archive / "source-snapshot"))
    retried, reused = [], []
    for n in manifest["tasks"]:
        task = root / f"task-{n:02d}"
        path = task / "controls.json"
        if n in exclusions:
            shutil.copytree(task, archive / task.name)
        elif path.exists() and json.loads(path.read_text()).get("passed"):
            reused.append(n)
        else:
            retried.append(n)
            if task.exists():
                shutil.move(str(task), str(archive / task.name))
    audit = {"at": now(), "reason": "Explicit pre-model technical repair; no task replacement or score-based selection",
             "archive": str(archive.relative_to(root)), "retry_tasks": retried, "reused_control_tasks": reused,
             "retained_excluded_control_tasks": list(exclusions),
             "prior_source_hashes": prior, "new_source_hashes": source_hashes,
             "protected_functions_unchanged": list(protected), "control_execution_policy": policy, "model_tokens": 0}
    save(archive / "repair.json", audit)
    manifest.setdefault("control_repairs", []).append(audit)
    manifest.update(status="validating", source_hashes=source_hashes, control_execution_policy=policy,
                    version="harness-v8-control-repair")
    manifest.pop("control_errors", None)
    save(root / "manifest.json", manifest)
    for key in source_hashes:
        destination = root / "source-snapshot" / key
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(LAB / key, destination)
    print(f"Control repair: preserve {len(reused)} passed tasks; retry {retried}; originals archived", flush=True)


def resume_batch(source, root, source_hashes, task_numbers, setups, model, reasoning):
    """Explicit new attempt: reuse controls/results, never partial model context."""
    if root.exists():
        raise RuntimeError("Resume destination must be a new batch")
    prior = json.loads((source / "manifest.json").read_text())
    if (prior["tasks"], prior["setups"], prior["model"], prior["reasoning"]) != (task_numbers, setups, model, reasoning):
        raise RuntimeError("Resume must preserve task/setup/model selection")
    old_hashes = prior.get("execution_source_hashes", prior["source_hashes"])
    runner_key = str((SOURCE_DIR / "run.py").relative_to(LAB))
    changed = {k for k in old_hashes.keys() | source_hashes.keys() if old_hashes.get(k) != source_hashes.get(k)}
    if changed - {runner_key}:
        raise RuntimeError("Resume requires unchanged evaluator, dataset, prompts and dependency images")
    old_directory = source / ("execution-source-snapshot" if (source / "execution-source-snapshot").exists() else "source-snapshot")
    old_ast = ast.parse((old_directory / runner_key).read_text())
    new_ast = ast.parse((SOURCE_DIR / "run.py").read_text())
    protected = ("evaluate", "container", "trial", "model_stage", "role_instructions", "issue_prompt", "network_checks", "valid_patch", "validate_task_controls", "task_controls")
    for name in protected:
        def body(tree):
            return next(n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name)
        if ast.dump(body(old_ast)) != ast.dump(body(new_ast)):
            raise RuntimeError(f"Resume protected behavior changed: {name}")
    excluded = prior.get("control_exclusions", [])
    carried, retry = [], []
    for n in task_numbers:
        task = source / f"task-{n:02d}"
        controls = json.loads((task / "controls.json").read_text())
        if not controls.get("passed") and n not in excluded:
            raise RuntimeError(f"Task {n}: controls not passed or explicitly excluded")
        if n not in excluded and not (task / "preparation/snapshot.json").is_file():
            raise RuntimeError(f"Task {n}: missing prepared snapshot")
        for selected in setups:
            result = task / selected / "result.json"
            done = result.is_file() and json.loads(result.read_text()).get("status") not in ("technical_interruption", "evaluation_problem")
            (carried if done else retry).append({"task": n, "setup": selected})
    # Validate every input before creating the destination. Preserve original batch.
    root.mkdir(mode=0o700)
    for n in task_numbers:
        task = source / f"task-{n:02d}"
        destination = root / task.name; destination.mkdir()
        for name in ("controls.json", "controls-original", "controls-reference", "preparation"):
            item = task / name
            if item.is_dir(): shutil.copytree(item, destination / name)
            elif item.is_file(): shutil.copy2(item, destination / name)
        for entry in carried:
            if entry["task"] == n:
                shutil.copytree(task / entry["setup"], destination / entry["setup"])
    manifest = {k: prior[k] for k in ("tasks", "setups", "model", "reasoning", "auth_mode", "network_policy", "model_timeout_seconds", "evaluation_timeout_seconds", "control_marker_patch_sha256", "selection_file", "selection_size", "control_execution_policy", "control_exclusions") if k in prior}
    manifest.update(version="harness-v9-model-workers", created_at=now(), status="controls_passed", source_hashes=source_hashes,
        resume={"source_batch": source.name, "at": now(), "source_hashes": old_hashes,
                "carried_results": carried, "fresh_trials": retry, "controls_reexecuted": False,
                "reason": "Explicit restart after technical interruption; partial model stages are not reused"})
    save(root / "manifest.json", manifest)
    for key in source_hashes:
        dest = root / "source-snapshot" / key; dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(LAB / key, dest)
    print(f"Resume: reuse controls and {len(carried)} recorded results; {len(retry)} fresh trials; source preserved", flush=True)


def resume_in_place(root, source_hashes, task_numbers, setups, model, reasoning):
    """Validate first, archive incomplete trials; retain original controls/results."""
    with tempfile.TemporaryDirectory(prefix="swe-resume-plan-", dir=root.parent) as temporary:
        plan = Path(temporary) / "plan"
        resume_batch(root, plan, source_hashes, task_numbers, setups, model, reasoning)
        manifest = json.loads((plan / "manifest.json").read_text())
        old_bytes = (root / "manifest.json").read_bytes()
        archive = root / "technical-interruptions" / ("model-resume-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:6])
        archive.mkdir(parents=True)
        (archive / "manifest.json").write_bytes(old_bytes)
        moved = []
        installed_snapshot = False
        try:
            for name in ("source-snapshot", "execution-source-snapshot"):
                source = root / name
                if source.exists():
                    destination = archive / name
                    shutil.move(str(source), str(destination)); moved.append((source, destination))
            for entry in manifest["resume"]["fresh_trials"]:
                source = root / f"task-{entry['task']:02d}" / entry["setup"]
                if source.exists():
                    destination = archive / source.relative_to(root)
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(source), str(destination)); moved.append((source, destination))
            shutil.move(str(plan / "source-snapshot"), str(root / "source-snapshot"))
            installed_snapshot = True
            manifest["resume"].update(in_place=True, archive=str(archive.relative_to(root)))
            previous = json.loads(old_bytes)
            manifest["resume_history"] = previous.get("resume_history", []) + [manifest["resume"]]
            save(archive / "resume.json", manifest["resume"])
            save(root / "manifest.json", manifest)
        except BaseException:
            if installed_snapshot:
                shutil.rmtree(root / "source-snapshot", ignore_errors=True)
            for source, destination in reversed(moved):
                if destination.exists():
                    source.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(destination), str(source))
            (root / "manifest.json").write_bytes(old_bytes)
            raise
    print(f"Resume in {root.name}: controls/results retained; incomplete attempts archived under {archive.relative_to(root)}", flush=True)


def recorded_execution_mode(root, manifest):
    if manifest.get("execution_mode") is not None:
        return manifest["execution_mode"]
    carried = {(x["task"], x["setup"]) for x in manifest.get("resume", {}).get("carried_results", [])}
    modes = set()
    for marker in root.glob("task-*/*/started.json"):
        identity = (int(marker.parent.parent.name.removeprefix("task-")), marker.parent.name)
        if identity in carried:
            continue
        modes.add(json.loads(marker.read_text()).get("execution_mode", "sequential"))
    if len(modes) > 1:
        raise RuntimeError("Conflicting execution modes in model start markers")
    return next(iter(modes), None)


async def main(run_models, task_numbers, batch, setup="both", parallel=False, model="gpt-6-luna", reasoning="medium",
               parallel_controls=False, control_workers=2, repair_controls=False, exclude_invalid_controls=None,
               model_workers=None, resume_from=None):
    global RUN_MODEL, RUN_REASONING
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", model):
        raise ValueError("Use a native Codex model ID, for example gpt-6-luna")
    if reasoning not in ("low", "medium", "high", "xhigh", "max"):
        raise ValueError("Unsupported reasoning level")
    RUN_MODEL, RUN_REASONING = model, reasoning
    if repair_controls and run_models:
        raise ValueError("--repair-controls cannot be combined with --run; validate repairs before starting models")
    if control_workers < 1:
        raise ValueError("Control workers must be positive")
    selection_path, selection = load_selection(HERE)
    if sha(DATA / "swebench_pro_verified.jsonl") != selection["dataset_sha256"]:
        raise RuntimeError("Preregistered dataset hash mismatch")
    setups = ["standard", "roles-b"] if setup == "both" else [setup]
    root = HERE / batch
    if resume_from and (not run_models or repair_controls):
        raise ValueError("--resume-from requires --run and cannot repair controls")
    if model_workers is not None and (model_workers < 1 or not parallel):
        raise ValueError("--model-workers requires --parallel and a positive value")
    if not resume_from:
        root.mkdir(exist_ok=True, mode=0o700)
    manifest_path = root / "manifest.json"
    if manifest_path.exists():
        recorded = json.loads(manifest_path.read_text())
        if (recorded["status"] == "completed" or
                (recorded["status"] == "technical_interruption" and not repair_controls)) and not resume_from:
            if recorded["tasks"] != task_numbers or recorded["setups"] != setups:
                raise RuntimeError("Batch task/setup selection differs; use a separate batch")
            if recorded["model"] != model or recorded["reasoning"] != reasoning:
                raise RuntimeError("Batch model/reasoning differs; use a separate batch")
            # No execution occurs: newer central sources cannot rewrite historical runs.
            print(f"Batch already {recorded['status']}; no implicit repeats", flush=True)
            return 0 if recorded["status"] == "completed" else 2
    await ensure_evaluation_scripts(task_numbers, selection)
    source_hashes = {str(path.relative_to(LAB)): sha(path) for path in
        (SOURCE_DIR / "run.py", SOURCE_DIR / "runner_helpers.py", SOURCE_DIR / "report.py", SOURCE_DIR / "egress_proxy.py", SOURCE_DIR / "requirements.toml", selection_path,
         UPSTREAM / "benchmarks/swebench_pro_verified/swebench_pro_verified.py",
         UPSTREAM / "harnesses/codex.py", UPSTREAM / "harnesses/codex_roles_b.py",
         UPSTREAM / "environments/docker.py", UPSTREAM / "environments/docker_egress_proxy.py")}
    if (HERE / "experiment.json").is_file():
        source_hashes[str((HERE / "experiment.json").relative_to(LAB))] = sha(HERE / "experiment.json")
    if (DATA / "dependency-cache-overrides.json").is_file():
        source_hashes[str((DATA / "dependency-cache-overrides.json").relative_to(LAB))] = sha(DATA / "dependency-cache-overrides.json")
    for number in task_numbers:
        instance_id = selection["scored_tasks"][number - 1]["instance_id"]
        for path in sorted((DATA / "run_scripts" / instance_id).rglob("*")):
            if path.is_file():
                source_hashes[str(path.relative_to(LAB))] = sha(path)
    if resume_from:
        if not re.fullmatch(r"batch-[A-Za-z0-9][A-Za-z0-9_-]*", resume_from):
            raise ValueError("Resume source must be an existing batch name")
        source = HERE / resume_from
        if source == root:
            resume_in_place(root, source_hashes, task_numbers, setups, model, reasoning)
        else:
            resume_batch(source, root, source_hashes, task_numbers, setups, model, reasoning)
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        if repair_controls:
            if manifest["tasks"] != task_numbers or manifest["setups"] != setups or manifest["model"] != model or manifest["reasoning"] != reasoning:
                raise RuntimeError("Control repair must preserve task/setup/model selection")
            repair_control_attempt(root, manifest, source_hashes,
                                   {"mode": "parallel" if parallel_controls else "sequential",
                                    "workers": control_workers if parallel_controls else 1},
                                   manifest.get("control_exclusions", []) if exclude_invalid_controls is None else exclude_invalid_controls)
        if manifest["source_hashes"] != source_hashes:
            raise RuntimeError("Versioned sources changed since validation; create a new batch or explicitly invalidate controls")
        if manifest["model"] != model or manifest["reasoning"] != reasoning:
            raise RuntimeError("Batch model/reasoning differs; use a separate batch")
        if manifest.get("execution_source_hashes", source_hashes) != source_hashes:
            raise RuntimeError("Execution sources changed since the first model start; use a new batch")
        requested_mode = "parallel" if parallel else "sequential"
        prior_mode = recorded_execution_mode(root, manifest)
        if run_models and prior_mode is not None and prior_mode != requested_mode:
            raise RuntimeError("Execution mode is frozen after the first model start; use a new batch")
        if manifest["tasks"] != task_numbers or manifest["setups"] != setups:
            raise RuntimeError("Batch task/setup selection differs; use a separate batch")
        if manifest["status"] in ("completed", "technical_interruption"):
            print(f"Batch already {manifest['status']}; no implicit repeats", flush=True)
            return 0 if manifest["status"] == "completed" else 2
    else:
        if repair_controls:
            raise RuntimeError("--repair-controls requires an existing batch")
        manifest = {"version": "harness-v8-control-repair", "created_at": now(), "status": "validating",
                    "tasks": task_numbers, "setups": setups, "model": RUN_MODEL,
                    "selection_file": str(selection_path.relative_to(LAB)), "selection_size": len(selection["scored_tasks"]),
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
    if wanted != instances.keys():
        raise RuntimeError("Selected instances missing from the pinned dataset")
    excluded = sorted(set(manifest.get("control_exclusions", []) if exclude_invalid_controls is None else exclude_invalid_controls))
    if not set(excluded) <= set(task_numbers):
        raise ValueError("Excluded controls must belong to this batch")
    if manifest.get("execution_started_at") and excluded != manifest.get("control_exclusions", []):
        raise RuntimeError("Control exclusions are frozen after the first model start")
    for number in excluded:
        task = root / f"task-{number:02d}"
        controls = task / "controls.json"
        if not controls.exists() or json.loads(controls.read_text()).get("passed"):
            raise RuntimeError(f"Task {number}: explicit exclusion requires an existing failed control result")
        for selected_setup in setups:
            save(task / selected_setup / "result.json", {"status": "control_excluded", "resolved": None,
                "setup": selected_setup, "model": model, "stages": [], "model_tokens": 0,
                "reason": "Explicit symmetric exclusion after failed pre-model controls; not a model failure",
                "control_result": "../controls.json"})
    if excluded:
        manifest["control_exclusions"] = excluded
        save(manifest_path, manifest)
        print(f"Explicit unscored control exclusions for both setups: {excluded}; no replacement tasks", flush=True)
        cases = [(n, case) for n, case in cases if n not in excluded]
    workers = control_workers if parallel_controls else 1
    pending_controls = any(not (root / f"task-{n:02d}" / "controls.json").exists() for n, _ in cases)
    policy = {"mode": "parallel" if parallel_controls else "sequential", "workers": workers}
    if pending_controls:
        if manifest.get("control_execution_policy", policy) != policy:
            raise RuntimeError("Control execution policy is frozen; use a new batch")
        manifest["control_execution_policy"] = policy
        save(manifest_path, manifest)
    if pending_controls:
        print(f"Controls: {policy['mode']}, at most {workers} task pipelines; model tokens 0", flush=True)
    else:
        print("Controls: reusing recorded results; no new control executions", flush=True)
    snapshots = await task_controls(cases, instances, root, manifest, manifest_path, workers)
    if snapshots is None:
        return 2
    for number, case in cases:
        ORIGINAL_IMAGES[case["instance_id"]] = snapshots[number]["original_image_id"]
        BASE_COMMITS[snapshots[number]["prepared_image_id"]] = case["base_commit"]
        IMAGE_LANGUAGES[snapshots[number]["prepared_image_id"]] = case["repo_language"]
    manifest.pop("control_errors", None)
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
    if manifest.get("execution_started_at") and "model_workers" in manifest and manifest["model_workers"] != (model_workers if parallel else 1):
        raise RuntimeError("Model worker count is frozen; use a new resume batch")
    manifest.update(model_workers=model_workers if parallel else 1, execution_mode="parallel" if parallel else "sequential",
                    execution_runner_version="harness-v8-control-repair",
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
            result = await parallel_trials(jobs, manifest, manifest_path, Path(private), credential.read_bytes(), model_workers)
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
    return (model or recorded.get("model") or config.get("model", "gpt-6-sol"),
            reasoning or recorded.get("reasoning") or config.get("reasoning", "medium"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subscription benchmark; fixed preregistered selection, no model deadline")
    parser.add_argument("--experiment", required=True, help="Output/selection directory inside the lab, for example experiment-luna-01")
    parser.add_argument("--run", action="store_true", help="Run selected model trials after passing controls; consumes subscription capacity")
    parser.add_argument("--parallel", action="store_true", help="With --run, run task/setup trials concurrently, bounded by --model-workers")
    parser.add_argument("--model-workers", type=int, help="Maximum concurrent task/setup model trials with --parallel (default: 2)")
    parser.add_argument("--resume-from", help="Stopped batch: reuse controls/results; same as --batch archives incomplete attempts in place, otherwise creates a new batch")
    parser.add_argument("--parallel-controls", action="store_true", help="Prepare and validate tasks concurrently, bounded by --control-workers; no model tokens")
    parser.add_argument("--control-workers", type=int, default=2, help="Maximum concurrent task preparation/control pipelines with --parallel-controls (default: 2)")
    parser.add_argument("--selection", help="Pin a lab task pool for a new experiment, e.g. selection-extended.json; subsequent batches reuse it automatically")
    parser.add_argument("--repair-controls", action="store_true", help="Before any models: archive failed/missing control attempts, retain passed controls, refreeze an unchanged evaluator with repaired runner")
    parser.add_argument("--exclude-invalid-controls", help="Explicit symmetric, unscored exclusion of failed control tasks, e.g. 65; frozen before model execution; never replaces tasks")
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
    if args.list:
        try:
            _, selection = load_selection(HERE, args.selection)
        except (ValueError, FileNotFoundError) as error:
            parser.error(str(error))
        for number, case in enumerate(selection["scored_tasks"], 1):
            print(f"{number:2d}  {case['repo_language']:6s}  {case['repo']}  {case['instance_id']}")
        raise SystemExit(0)
    if not args.batch or not re.fullmatch(r"batch-[A-Za-z0-9][A-Za-z0-9_-]*", args.batch):
        parser.error("--batch is required and must be a separate name such as batch-02")
    if not args.tasks and not args.next_count:
        parser.error("Specify --tasks 4-6 or --next 3")
    if args.next_count is not None and args.next_count < 1:
        parser.error("--next must be positive")
    if args.control_workers < 1:
        parser.error("--control-workers must be positive")
    if args.repair_controls and args.run:
        parser.error("--repair-controls cannot be combined with --run")
    if not args.parallel_controls and args.control_workers != 2:
        parser.error("--control-workers requires --parallel-controls")
    if args.model_workers is not None and (args.model_workers < 1 or not args.parallel):
        parser.error("--model-workers requires --parallel and a positive value")
    if args.parallel and args.model_workers is None:
        args.model_workers = 2
    if args.resume_from and (not args.run or args.repair_controls):
        parser.error("--resume-from requires --run and cannot repair controls")
    HERE.mkdir(exist_ok=True, mode=0o700)
    args.model, args.reasoning = resolve_model_configuration(HERE, args.batch, args.model, args.reasoning)
    with (HERE / ".runner.lock").open("a") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.error("Another coordinator is already running for this experiment; stop it before resuming")
        try:
            _, selection = load_selection(HERE, args.selection, pin=True)
            numbers = select_tasks(args.tasks, args.next_count, selection, HERE, args.batch)
            exclusions = select_tasks(args.exclude_invalid_controls, None, selection, HERE, args.batch) if args.exclude_invalid_controls else None
        except (ValueError, FileNotFoundError) as error:
            parser.error(str(error))
        print(f"Experiment {HERE.name}; batch {args.batch}: tasks {numbers}, setup {args.setup}, {args.model}/{args.reasoning}, no model deadline", flush=True)
        try:
            result = asyncio.run(main(args.run, numbers, args.batch, args.setup, args.parallel, args.model, args.reasoning,
                                      args.parallel_controls, args.control_workers, args.repair_controls, exclusions, args.model_workers, args.resume_from))
        except KeyboardInterrupt:
            path = HERE / args.batch / "manifest.json"
            if path.is_file():
                manifest = json.loads(path.read_text())
                manifest.update(status="technical_interruption", interrupted_at=now(),
                                interruption_reason="Coordinator stopped with Ctrl+C; preserve partial trials and use --resume-from")
                save(path, manifest)
            print("Stopped; logs and controls preserved. Use a new batch with --resume-from to restart incomplete trials.", flush=True)
            raise SystemExit(130)
        raise SystemExit(result)
