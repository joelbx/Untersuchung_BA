Task: implement predictable no_log value and key sanitization in basic.py and update uri use.
Status: implemented separate iterative value and key sanitizers, updated uri to sanitize response keys with NO_MODIFY_KEYS, and adjusted date JSON encoding plus focused tests.
Verification: focused no_log, exit_json, and heuristic_log_sanitize tests pass (31). The full basic suite has unrelated shared warning state failures when run together; deprecate_warn also fails on shared warning state in isolation.
Constraints: local repository and existing tests only; preserve git history, index, and harness configuration.
