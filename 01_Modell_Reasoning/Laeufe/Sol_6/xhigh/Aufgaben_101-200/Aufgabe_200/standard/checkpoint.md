# Checkpoint

- Task: add unit-aware durations to `:later` while preserving bare integer milliseconds.
- Located command in `qutebrowser/misc/utilcmds.py` and parser target in `qutebrowser/utils/utils.py`.
- Implemented `parse_duration`, wired `:later` to it, updated command help, and added parser and command tests.
- Verification: 194 tests passed in the two affected unit test modules using `xvfb-run -a` with the pytest Xvfb plugin disabled; `git diff --check` passed.
