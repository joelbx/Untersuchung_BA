# Checkpoint

Task: Support Jinja2 keyword arguments in Ansible's `min` and `max` filters.

Implemented in `lib/ansible/plugins/filter/mathstuff.py`: both filters use `@environmentfilter`, forward every keyword argument to the corresponding Jinja2 filter when available, and use Python's built-in filter without keywords otherwise. Keyword arguments in fallback mode raise the required `AnsibleFilterError` message.

Updated unit tests for attribute selection, case sensitivity, arbitrary keyword forwarding, and fallback behavior. Updated integration assertions for attribute and case sensitivity when Jinja2 provides both filters.

Checks:
- `PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py` — 57 passed.
- Local Ansible `Templar` rendered `max(attribute="block_total")` to 8, `min(attribute="block_total")` to 1, and case-sensitive min/max to `B`/`a`.
- `git diff --check` — passed.

Environment notes:
- `rg` was unavailable: `/bin/bash: rg: command not found`; used `find` and `grep`.
- Initial `python -m pytest -q test/units/plugins/filter/test_mathstuff.py` imported installed Ansible at `/usr/local/lib/python3.9/dist-packages/ansible/plugins/filter/mathstuff.py` and failed 10 tests; rerunning with `PYTHONPATH=lib` tested the checkout and passed.
