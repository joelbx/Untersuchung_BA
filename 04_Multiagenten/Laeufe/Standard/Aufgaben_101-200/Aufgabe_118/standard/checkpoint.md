Task: Fix pip module fallback when no pip executable is on PATH.
Status: Complete.
Changes: Added interpreter-based pip launcher with importability detection and safe fallback; normalized launchers to argv; updated package listing to use argv and return a command string; built virtualenv path prefix with os.path.join. Added focused unit coverage.
Validation: PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py (9 passed); git diff --check passed.
Constraints observed: Local repository only; no git history, index baseline, or harness changes.
