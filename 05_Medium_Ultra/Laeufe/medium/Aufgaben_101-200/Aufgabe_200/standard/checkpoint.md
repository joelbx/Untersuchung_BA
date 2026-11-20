Task: Add unit-aware durations to :later.
Status: Implemented parse_duration in qutebrowser/utils/utils.py; :later now parses duration strings. Updated command help and unit tests.
Verification: Focused duration/later tests: 26 passed, exit 0. Full relevant unit files: 190 passed, but pytest process exited 1 after X11 connection broke during shutdown. git diff --check passed.
Constraints observed: local repository only; no git history, index baseline, or harness configuration changes.
