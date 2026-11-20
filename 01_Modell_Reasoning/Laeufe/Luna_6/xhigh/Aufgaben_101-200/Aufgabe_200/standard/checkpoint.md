# Checkpoint

Task: Add explicit duration units to qutebrowser's `:later` command while preserving numeric millisecond input.

Plan:
- Inspect repository guidance and current duration/command parsing paths.
- Implemented public `parse_duration` in `qutebrowser/utils/utils.py`; it accepts ordered h/m/s components, decimal amounts, inter-unit whitespace, and legacy integer milliseconds.
- Updated `:later` to parse a duration string and turn invalid input into a command error while preserving the original timer behavior.
- Run relevant existing tests and report results.

Constraints: Do not change git history, index baseline, or harness configuration.

Validation:
- `pytest -q tests/unit/utils/test_utils.py tests/unit/misc/test_utilcmds.py` — 164 passed.
- `git diff --check` — clean.
