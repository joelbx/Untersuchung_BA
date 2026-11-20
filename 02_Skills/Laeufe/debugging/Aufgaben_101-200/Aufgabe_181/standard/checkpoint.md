# Process message issue checkpoint

Phase: root cause investigation started.

Repository search: `rg` unavailable (`/bin/bash: rg: command not found`); using `find`/`grep`.

Baseline check: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/misc/test_guiprocess.py` exited 4 while loading conftest: `ModuleNotFoundError: No module named 'PyQt5'`. This prevents running the repository Qt tests offline. I will add focused unit tests and use a local standard-library reproduction for executable verification.

Root cause: `_on_finished` builds errors with a bare `:process`, which resolves via mutable global `last_pid`; it also groups every non-success exit into `message.error`. `ProcessOutcome.__str__` reduces every CrashExit to `crashed`, and `state_str` has no SIGTERM branch. Similar working behavior in the same module already uses `self.pid` for stdout/stderr replacement and uses `verbose` to gate successful info messages. Hypothesis: using `self.pid` in each finished message and a separate `was_sigterm()` branch restores correct routing and notification level; signal formatting should derive its name from the crash exit code.

Implementation: Added `ProcessOutcome.was_sigterm`, signal-aware outcome text, and `terminated` completion state. Finished messages now include `self.pid` in `:process` and use info for verbose successful/SIGTERM outcomes, errors for other failures; quiet SIGTERM has no finished message. Added Qt regression tests for all affected outcomes.

Reproduction: `/tmp/repro_guiprocess_outcome.py` failed before the fix with `AttributeError: 'ProcessOutcome' object has no attribute 'was_sigterm'`. After the fix, `python /tmp/repro_guiprocess_outcome.py` exited 0 and checked outcome text/state and finished-message content/levels for success, nonzero exit, SIGSEGV, and SIGTERM in both verbosity modes.

Verification: `python -m compileall -q qutebrowser/misc/guiprocess.py tests/unit/misc/test_guiprocess.py` and `git diff --check` exited 0. Re-running `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/misc/test_guiprocess.py` exited 4 before test collection: `ModuleNotFoundError: No module named 'PyQt5'` in `qutebrowser/qt/core.py:12`. Thus actual Qt signal delivery and the repository tests remain unverified in this environment; no dependencies were downloaded.
