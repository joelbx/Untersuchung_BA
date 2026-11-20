Task: support Jinja2 keyword arguments in min/max filters with builtin fallback.
Status: implementation and focused tests complete.
Verification: PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py (57 passed); git diff --check passed.
