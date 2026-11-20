# Checkpoint

Implemented process completion messages with the specific PID, named signals for crashes, SIGTERM detection and `terminated` state. Quiet SIGTERM exits produce no completion message; verbose exits include the outcome and `:process <pid>` reference. Updated unit and end-to-end expectations.

Checks:
- `git diff --check` — passed.
- `python -m compileall -q qutebrowser/misc/guiprocess.py tests/unit/misc/test_guiprocess.py` — passed.
- `pytest -q tests/unit/misc/test_guiprocess.py` — blocked before collection by missing local dependency. Exact error: `ModuleNotFoundError: No module named 'PyQt5'` while importing `qutebrowser.qt.core` from `tests/helpers/messagemock.py` through `tests/conftest.py`. The behavior of live QProcess signals and messages remains unverified in this environment.
