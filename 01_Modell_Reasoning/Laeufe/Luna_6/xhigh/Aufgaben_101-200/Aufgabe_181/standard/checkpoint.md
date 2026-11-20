# Checkpoint

Task: Improve Qute browser process-finish outcomes and messages.

Implemented:
- Added `ProcessOutcome.was_sigterm()` and SIGTERM-specific outcome text/state (`terminated`).
- Crash outcomes now show a recognized signal name.
- Finish messages include `:process <pid>`; verbose success and SIGTERM messages are informational, and non-verbose SIGTERM finish messages are suppressed.
- Updated existing assertions for the changed success, failure, and crash messages.

Validation:
- `python -m py_compile qutebrowser/misc/guiprocess.py tests/unit/misc/test_guiprocess.py` passed.
- `git diff --check` passed.
- `python -m pytest tests/unit/misc/test_guiprocess.py -q` could not load `tests/conftest.py`: PyQt5 is not installed in this checkout. No dependencies were installed.
