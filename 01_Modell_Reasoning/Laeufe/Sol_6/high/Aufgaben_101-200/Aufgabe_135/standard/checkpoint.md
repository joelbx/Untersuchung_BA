Task: support Jinja2 keyword arguments in Ansible min/max filters.
Status: complete. min/max receive the environment, forward all keyword arguments to Jinja2 do_min/do_max when present, and use Python built-ins without keywords or raise the specified AnsibleFilterError on fallback.
Verification: PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py (57 passed); git diff --check passed.
