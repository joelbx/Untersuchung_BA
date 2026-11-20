# Checkpoint

Issue: Populate Linux hardware facts from `/proc/sysinfo` on IBM Z / s390.

Status: Implemented `/proc/sysinfo` parsing and merged the resulting fields into Linux hardware facts after DMI facts. Added tests for absent and partial files, parsed values, and collector integration.

Checks:
- `python -m pytest -q test/units/module_utils/facts/hardware/test_linux.py` — 15 passed.
- `git diff --check` — passed.

Repository search note: `rg` is unavailable (`/bin/bash: rg: command not found`); used `grep` and `find`.
