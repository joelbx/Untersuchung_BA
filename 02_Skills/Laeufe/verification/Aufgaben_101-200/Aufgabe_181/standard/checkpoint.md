# Process message fix checkpoint

Issue: Correct process PID in finish messages, suppress nonverbose SIGTERM errors, and show signal names and terminated state.

Initial inspection: `qutebrowser/misc/guiprocess.py` builds failure messages using bare `:process`, reports all crashes generically, and has no SIGTERM state. Related tests are in `tests/unit/misc/test_guiprocess.py`.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); using local file search instead.

Verification attempt before implementation: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/misc/test_guiprocess.py` exited 4 while importing `tests/conftest.py`: `ModuleNotFoundError: No module named 'PyQt5'`. The red/green behavior of the tests cannot be observed in this environment.

Implemented: `ProcessOutcome.was_sigterm()`; SIGTERM outcome text/state; signal names for other crashes; finish messages with `self.pid`; nonverbose SIGTERM notification suppression. Updated process tests and added a distinct `last_pid` regression case.

Final checks:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/misc/test_guiprocess.py` exited 4 with `ModuleNotFoundError: No module named 'PyQt5'` during `tests/conftest.py` import. Test behavior remains unverified because the local Qt dependency is unavailable.
- `python -m compileall -q qutebrowser/misc/guiprocess.py tests/unit/misc/test_guiprocess.py` exited 0.
- `git diff --check` exited 0.
