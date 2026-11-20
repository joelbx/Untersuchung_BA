"""Local task selection and conservative evidence of actual test execution."""
import json
import re
import shlex
import random


def expanded_selection(original, rows):
    """Keep the original scored prefix; deterministically order remaining tasks."""
    by_id = {row["instance_id"]: row for row in rows}
    if len(by_id) != len(rows):
        raise ValueError("Duplicate dataset instance IDs")
    prefix = original["scored_tasks"]
    used = {case["instance_id"] for case in prefix}
    used.add(original["smoke_test"]["instance_id"])
    if len(used) != len(prefix) + 1 or not used <= by_id.keys():
        raise ValueError("Original selection is not a unique dataset subset")
    remaining = [by_id[key] for key in sorted(by_id.keys() - used)]
    random.Random(original["selection_seed"]).shuffle(remaining)
    fields = ("instance_id", "repo", "repo_language", "base_commit", "dockerhub_tag")
    return {**original, "selection_rule": original["selection_rule"] +
            "; extension: retain original scored prefix; exclude smoke; sort remaining instance IDs, "
            "shuffle using a fresh random.Random(selection_seed), append all remaining public tasks",
            "original_scored_prefix_count": len(prefix),
            "scored_tasks": prefix + [{key: row[key] for key in fields} for row in remaining]}


def select_tasks(spec, next_count, selection, directory, batch):
    limit = len(selection["scored_tasks"])
    if spec:
        numbers = []
        for part in spec.split(","):
            if re.fullmatch(r"\d+-\d+", part):
                start, end = map(int, part.split("-"))
                if end < start:
                    raise ValueError("Task range must be ascending")
                numbers.extend(range(start, end + 1))
            elif part.isdigit():
                numbers.append(int(part))
            else:
                raise ValueError("Use task numbers such as 4-6 or 4,5,6")
        if len(set(numbers)) != len(numbers):
            raise ValueError("Duplicate task numbers")
    else:
        existing = directory / batch / "manifest.json"
        if existing.exists():
            numbers = json.loads(existing.read_text())["tasks"]
            if len(numbers) != next_count:
                raise ValueError("Existing batch has a different task count")
        else:
            used = set()
            for manifest in directory.glob("batch-*/manifest.json"):
                content = json.loads(manifest.read_text())
                # Reserve every assigned task, even in an interrupted batch.
                used.update(content["tasks"])
            numbers = [n for n in range(1, limit + 1) if n not in used][:next_count]
            if len(numbers) != next_count:
                raise ValueError("Not enough unused preregistered tasks")
    if not numbers or any(n < 1 or n > limit for n in numbers):
        raise ValueError(f"Task numbers must be between 1 and {limit}")
    return numbers


def shell_body(command):
    try:
        outer = shlex.split(command)
    except ValueError:
        return ""
    if len(outer) >= 3 and outer[0].rsplit("/", 1)[-1] in ("bash", "sh") and "c" in outer[1]:
        command = outer[2]
    return re.sub(r"(?ms)^[^\n]*<<-?\s*['\"]?(\w+)['\"]?[^\n]*\n.*?^\1\s*$", "", command)


def test_kind(command):
    for segment in re.split(r"[;&|\n]+", shell_body(command)):
        try:
            words = shlex.split(segment)
        except ValueError:
            continue
        while words and re.match(r"^[A-Za-z_][A-Za-z_0-9]*=", words[0]):
            words.pop(0)
        # Only recognized launcher prefixes; arbitrary shell scripts cannot
        # establish evidence just by mentioning a test command.
        if words and words[0].rsplit("/", 1)[-1] == "env":
            words.pop(0)
            while words and re.match(r"^[A-Za-z_][A-Za-z_0-9]*=", words[0]):
                words.pop(0)
        if words and words[0].rsplit("/", 1)[-1] == "timeout":
            words.pop(0)
            while words and words[0].startswith("-"):
                words.pop(0)
            if words:
                words.pop(0)
        if words and words[0].rsplit("/", 1)[-1] in ("dbus-run-session", "xvfb-run"):
            words.pop(0)
            while words and words[0].startswith("-"):
                words.pop(0)
        if not words:
            continue
        executable = words[0].rsplit("/", 1)[-1]
        if executable == "go" and words[1:2] == ["test"]:
            return "go"
        if executable in ("pytest", "py.test"):
            return "python"
        if re.fullmatch(r"python(?:\d+(?:\.\d+)*)?", executable) and "-m" in words:
            index = words.index("-m")
            if words[index + 1:index + 2] in (["pytest"], ["unittest"]):
                return "python"
        if executable == "ansible-test" and "units" in words:
            return "python"
        if executable in ("jest", "vitest", "mocha"):
            return "js"
        if executable in ("npm", "yarn", "pnpm") and any(
                re.fullmatch(r"test(?::[\w-]+)?", word) for word in words[1:]):
            return "js"
    return None


def review_test_evidence(events):
    attempts = []
    for event in events:
        item = event.get("item") or {}
        if event.get("type") != "item.completed" or item.get("type") != "command_execution":
            continue
        command = str(item.get("command") or "")
        kind = test_kind(command)
        if not kind:
            continue
        output = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", str(item.get("aggregated_output") or ""))
        failed = item.get("exit_code") != 0 or bool(re.search(
            r"(?m)^FAIL\b|\[build failed\]|\b[1-9]\d*\s+(?:failed|errors?)\b|^FAILED\s", output))
        if kind == "go":
            passed = bool(re.search(r"(?m)^ok\s", output) or '"Action":"pass"' in output)
            passed = passed and "[no tests to run]" not in output
        elif kind == "python":
            passed = bool(re.search(r"\b[1-9]\d*\s+passed\b", output) or
                          re.search(r"(?s)Ran [1-9]\d* tests?.*\nOK(?:\s|$)", output))
        else:
            passed = bool(re.search(r"(?m)^\s*Tests:\s*.*\b[1-9]\d* passed\b|\b[1-9]\d* passing\b", output))
        attempts.append({"command": command, "test_kind": kind, "exit_code": item.get("exit_code"),
                         "successful_test_evidence": passed and not failed,
                         "test_invocation_failed": failed})
    return {"attempts": attempts, "accept_supported": any(
        a["successful_test_evidence"] for a in attempts) and not any(a["test_invocation_failed"] for a in attempts)}
