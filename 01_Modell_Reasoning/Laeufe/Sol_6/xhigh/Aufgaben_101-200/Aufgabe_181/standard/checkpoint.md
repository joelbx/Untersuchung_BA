# Checkpoint

- Task: improve GUI process completion messages, PID accuracy, and SIGTERM handling.
- Repository: `/app`; working tree initially clean.
- Located implementation in `qutebrowser/misc/guiprocess.py` and existing tests in `tests/unit/misc/test_guiprocess.py`.
- Updated `ProcessOutcome` to detect SIGTERM, describe named crash signals, and expose the `terminated` state.
- Updated `GUIProcess` completion messages to include its own PID. SIGTERM is silent by default and informational in verbose mode.
- Expanded existing process tests for success, failure, crash, SIGTERM, and a changed `last_pid`.
- Verification: `xvfb-run -a env QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen pytest -p no:xvfb -q tests/unit/misc/test_guiprocess.py` passed (44 tests). `git diff --check` passed.
