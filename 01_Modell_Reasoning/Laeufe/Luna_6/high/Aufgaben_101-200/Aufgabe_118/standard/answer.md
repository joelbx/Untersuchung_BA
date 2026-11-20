Updated [pip.py](/app/lib/ansible/modules/pip.py) to fall back to the current interpreter’s `pip` module when no pip executable is found, normalize launchers to argv lists, return quoted listing commands for logging, and build virtualenv path prefixes with `os.path.join`.

Verification passed: `python -m pytest -q test/units/modules/test_pip.py` (4 tests) and `git diff --check`.