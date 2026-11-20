#!/usr/bin/env python3
"""Trusted host-only dependency prefetch; source/reference code is never retained.

Only go.mod/go.sum changes from the reference are temporarily applied. Download
both dependency sets, restore the canonical base, delete the patch, then commit
a dependency-cache overlay. TypeScript images additionally receive Node headers
and root-owned working directories for npm under restricted container capabilities.
No tests or compilation execute reference source.
"""
import argparse
import asyncio
import json
import tempfile
import uuid
from pathlib import Path

import run as runner


async def warm(selection, numbers):
    rows = {r["instance_id"]: r for r in map(json.loads, (runner.DATA / "swebench_pro_verified.jsonl").read_text().splitlines())}
    if runner.sha(runner.DATA / "swebench_pro_verified.jsonl") != selection["dataset_sha256"]:
        raise RuntimeError("Dataset hash mismatch")
    output = runner.DATA / "dependency-cache-overrides.json"
    overrides = json.loads(output.read_text()) if output.exists() else {}
    for number in numbers:
        case = selection["scored_tasks"][number - 1]
        if case["repo_language"] not in ("go", "ts"):
            raise RuntimeError("Only Go and TypeScript dependency caches are supported")
        directory = runner.LAB / "validation/dependency-cache" / f"task-{number:02d}"
        image = await runner.ensure_image("jefzda/sweap-images:" + case["dockerhub_tag"], directory)
        existing = overrides.get(case["instance_id"])
        if existing:
            if existing["official_image_id"] != image["Id"]:
                raise RuntimeError("Existing cache has different official origin")
            await runner.host(["docker", "image", "inspect", existing["cached_image_id"]])
            print(f"Task {number}: existing pinned dependency cache reused", flush=True)
            continue
        cid = None
        log = []
        async def command(argv, timeout=120):
            print(f"Task {number}: {' '.join(argv[:3])}", flush=True)
            result = await runner.host(["docker", "exec", cid, *argv], timeout=timeout)
            log.append({"command": argv, "stdout": result.stdout, "stderr": result.stderr, "exit_code": result.returncode})
            runner.save(directory / "commands.json", log)
            return result.stdout.strip()
        try:
            cid = (await runner.host(["docker", "run", "-d", "--network", "bridge", "--cpus", "4", "--memory", "8192m",
                "--name", "swe-dependency-prefetch-" + uuid.uuid4().hex[:12], "--workdir", "/app", "--entrypoint", "/bin/sh",
                image["Id"], "-c", "exec tail -f /dev/null"])).stdout.strip()
            await command(["git", "reset", "--hard", case["base_commit"]])
            before = await command(["git", "write-tree"])
            if case["repo_language"] == "go":
                print(f"Task {number}: downloading base Go dependencies; no model calls", flush=True)
                await command(["go", "mod", "download"], timeout=None)
                with tempfile.TemporaryDirectory(prefix="swe-trusted-dependencies-") as temporary:
                    patch = Path(temporary) / "reference.patch"
                    patch.write_text(rows[case["instance_id"]]["patch"])
                    await runner.host(["docker", "cp", str(patch), cid + ":/tmp/dependency-prefetch.patch"])
                await command(["git", "apply", "--include=go.mod", "--include=go.sum", "/tmp/dependency-prefetch.patch"])
                print(f"Task {number}: downloading reference manifest dependencies; no reference code executed", flush=True)
                await command(["go", "mod", "download"], timeout=None)
            else:
                # npm 8 attempts to spawn in the directory's group. Normalize
                # directory ownership, instead of granting SETUID/SETGID caps.
                await command(["find", "/app", "-type", "d", "-exec", "chown", "0:0", "{}", "+"], timeout=600)
                print(f"Task {number}: caching public Node headers; project/reference code unchanged", flush=True)
                await command(["/app/node_modules/.bin/node-gyp", "install", "--ensure"], timeout=None)
            await command(["git", "reset", "--hard", case["base_commit"]])
            await command(["rm", "-f", "/tmp/dependency-prefetch.patch"])
            after = await command(["git", "write-tree"])
            if before != after:
                raise RuntimeError("Reference dependency manifests were not restored")
            await command(["git", "diff", "--exit-code", case["base_commit"]])
            cached = (await runner.host(["docker", "commit", cid], timeout=300)).stdout.strip()
            overrides[case["instance_id"]] = {"official_image_id": image["Id"], "cached_image_id": cached,
                "base_commit": case["base_commit"], "canonical_tree": before,
                "dataset_sha256": selection["dataset_sha256"], "at": runner.now(),
                "reference_code_applied": False, "reference_source_executed": False, "model_tokens": 0}
            overrides[case["instance_id"]]["dependency_kind"] = "go-module-cache" if case["repo_language"] == "go" else "node-headers-and-directory-ownership"
            runner.save(output, overrides)
            print(f"Task {number}: cache ready; canonical source unchanged", flush=True)
        finally:
            if cid:
                await runner.host(["docker", "rm", "-f", cid], check=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", required=True, help="Comma-separated task numbers")
    args = parser.parse_args()
    selection = json.loads((runner.LAB / "selection-extended.json").read_text())
    numbers = [int(n) for n in args.tasks.split(",")]
    if not numbers or any(n < 1 or n > len(selection["scored_tasks"]) for n in numbers):
        parser.error("Invalid task numbers")
    asyncio.run(warm(selection, numbers))
