Task: Fix module shebang handling in /app.
Status: Implemented shebang extraction and preservation for new-style Python and other modules. Configured interpreter overrides retain precedence; default Python is used only when there is no module shebang. Added regression tests for versioned/custom Python, args, non-Python modules, overrides, discovery, and no shebang.
Verification: `python -m pytest -q test/units/executor --ignore=test/units/executor/test_task_executor.py` passed (86 tests, one ZipFile warning). `git diff --check` passed. Full executor collection is blocked by missing local `mock` package in `test_task_executor.py`.
Constraints: Use local code/tests only; preserve git history, index baseline, and harness configuration.
