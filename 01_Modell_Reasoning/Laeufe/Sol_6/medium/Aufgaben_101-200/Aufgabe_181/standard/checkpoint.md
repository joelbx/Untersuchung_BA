# Checkpoint

Task: Correct GUIProcess completion messages, PID reporting, and SIGTERM handling.
Status: Implementation and unit expectations updated.
Changes: ProcessOutcome detects SIGTERM and names crash signals; completion messages include the process's own PID; SIGTERM is silent unless verbose and has state `terminated`.
Verification: `git diff --check` and Python compileall passed. `pytest -q tests/unit/misc/test_guiprocess.py` could not start because PyQt5 is unavailable in this environment.
Constraints: Local repository only; git history, index baseline, and harness configuration preserved.
