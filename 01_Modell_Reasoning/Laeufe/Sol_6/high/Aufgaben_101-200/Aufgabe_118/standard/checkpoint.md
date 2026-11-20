Task: Fix pip module fallback when no pip executable is on PATH.
Status: Complete in working tree.
Changes: Detect pip importability with importlib.util.find_spec and pkgutil.find_loader fallback; use current interpreter with -m pip when available; normalize pip launcher to argv; use argv for list/freeze with string command logging; join virtualenv bin path with os.path.join; update documentation and unit tests.
Verification: PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py (12 passed); git diff --check (passed).
Constraints observed: local code/tests only; git history, index baseline, and harness configuration untouched.
