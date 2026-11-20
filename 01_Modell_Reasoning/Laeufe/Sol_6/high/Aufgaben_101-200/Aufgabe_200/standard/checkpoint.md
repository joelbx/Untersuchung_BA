# Checkpoint

Task: Add unit-aware durations to `:later` with `parse_duration` in `qutebrowser/utils/utils.py`.

Status: Complete. `parse_duration` supports ordered decimal h/m/s components with whitespace between units, preserves bare integer milliseconds, and rejects invalid input. `:later` uses the parser; help text and focused tests were updated.

Verification: `pytest -q tests/unit/utils/test_utils.py tests/unit/misc/test_utilcmds.py` (192 passed); `pytest -q tests/unit/misc/test_utilcmds.py tests/unit/commands` (207 passed, 1 skipped); `git diff --check` passed.
