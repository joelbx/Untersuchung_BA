# Checkpoint

Implemented process completion handling in `qutebrowser/misc/guiprocess.py`:

- Added `ProcessOutcome.was_sigterm()` using crash status and `signal.SIGTERM`.
- Included signal names in crash outcome text and represented SIGTERM as `terminated`.
- Added the actual process PID to completion messages. Successful outcomes are announced with the details link in verbose mode; SIGTERM is silent by default and reported in verbose mode.

Validation: `py_compile` and `git diff --check` pass. Focused pytest collection is blocked because PyQt5 is not installed (`ModuleNotFoundError`).
