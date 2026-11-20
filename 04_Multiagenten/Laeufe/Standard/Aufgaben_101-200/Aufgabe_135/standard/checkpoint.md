# Checkpoint

Task: enable Jinja2 keyword arguments for min/max filters with legacy fallback.
Status: complete.
Changed: mathstuff.py dispatches min/max to Jinja2 do_min/do_max with all keyword arguments when available; otherwise uses Python built-ins and raises the required AnsibleFilterError for keywords.
Tests: PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py (55 passed); git diff --check passed.
