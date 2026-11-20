Task: Fix pip module fallback when no pip executable exists and current interpreter has pip.
Status: Complete. The module now detects interpreter pip with importlib and a pkgutil fallback, uses an argv launcher for every pip selection, lists packages with modern and legacy commands, and derives virtualenv PATH prefix with os.path.join.
Verification: PYTHONPATH=lib PYTEST_ADDOPTS='' python -m pytest test/units/modules/test_pip.py -q (9 passed); git diff --check passed.
Files changed: lib/ansible/modules/pip.py, test/units/modules/test_pip.py.
