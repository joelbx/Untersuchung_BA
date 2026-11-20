Task: support Jinja2 min/max keyword arguments in lib/ansible/plugins/filter/mathstuff.py while preserving built-in fallback behavior.
Status: implementation and regression tests complete. Both filters use @environmentfilter, forward all keyword arguments to Jinja2 helpers when available, and raise the required AnsibleFilterError for keywords when a helper is unavailable. Calls without keywords use Python built-ins on fallback.
Verification: PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py (57 passed); git diff --check passed.
Delegation: none.
