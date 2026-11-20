# Checkpoint

Task: make `GuiProcess` stream both stdout and stderr live, and report nonempty final stream summaries in stdout-then-stderr order with appropriate severity.

Status: implementation and tests updated. `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`.

Verification: `pytest -q tests/unit/misc/test_guiprocess.py` exited 0 with 42 passed. `git diff --check` exited 0. The initial full test run failed in the new stderr live-output test because the test harness rejects uncaptured error logging; the test now captures the expected log and the fresh full rerun passed.
