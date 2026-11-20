# Checkpoint

Task: Update Ansible's `min` and `max` filters in `lib/ansible/plugins/filter/mathstuff.py` to delegate enhanced keyword arguments to Jinja2 filters when available, with the required compatibility error and builtin fallback.

Completed:
- Imported Jinja2's `do_min` and `do_max` independently when available.
- Decorated both filters with `@environmentfilter`; each delegates all keyword arguments to its corresponding Jinja filter, raises the specified `AnsibleFilterError` when that enhanced filter is unavailable and keywords are passed, and otherwise falls back to Python's builtin.
- Updated and expanded unit coverage for attribute, `case_sensitive`, unsupported keyword arguments, and fallback behavior.
- Ran `source hacking/env-setup && pytest -q test/units/plugins/filter/test_mathstuff.py`: 55 passed.
- `git diff --check` passed.
