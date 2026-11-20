# Checkpoint

Implemented optional `encoding` on `FormatString`, checked during `to_py` with the same validation error wording used by `String`. Configured `content.headers.user_agent` with ASCII. Added type-level tests for ASCII, Latin-1, and unrestricted values, plus a config-data test checking the real user-agent and title settings.

Checks:
- `pytest -q tests/unit/config/test_configtypes.py -k 'TestFormatString or TestString'`: 72 passed, 1046 deselected.
- `pytest -q tests/unit/config/test_configdata.py tests/unit/config/test_configtypes.py -k 'not benchmark'`: 1139 passed, 1 deselected, 10 xfailed.
- `git diff --check`: passed.

`rg` was unavailable (`/bin/bash: line 1: rg: command not found`); local `grep` was used for inspection. No offline check was blocked.
