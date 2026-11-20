Task: Fix pip module fallback to interpreter pip when no binary is on PATH.
Status: Implemented interpreter-based launcher detection, argv normalization, listing fallback, and virtualenv path prefix. Added focused tests. Verified: PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py (6 passed).
