Updated [aix.py](/app/lib/ansible/module_utils/facts/hardware/aix.py) to report a constant processor count of `1`, count available device rows as cores, default threads per core to `1`, derive vCPUs, and return the CPU type as a list.

Verification passed: `python -m pytest -q test/units/module_utils/facts/test_facts.py` — 91 passed, 5 skipped. `git diff --check` also passed.