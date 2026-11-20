# Checkpoint

Task completed: `min` and `max` are now environment filters that pass keyword arguments through to Jinja2's `do_min` and `do_max` when available. Missing enhanced filters produce the requested `AnsibleFilterError` for keyword calls, and no-keyword calls use Python's built-in behavior.

Updated the existing math filter unit tests to cover both enhanced filters and compatibility fallbacks.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py` passed (55 tests). `git diff --check` passed.
