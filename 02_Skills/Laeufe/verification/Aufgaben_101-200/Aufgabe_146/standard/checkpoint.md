# Checkpoint

Task: add IBM Z `/proc/sysinfo` hardware facts to the Linux setup collector.

Implemented `LinuxHardware.get_sysinfo_facts()` and merged its five identity fields into `populate()` after DMI facts. Added unit coverage for absent and present sysinfo, serial normalization, missing fields, and the populate merge.

Verification (fresh, after final edits):
- `python -m pytest -q test/units/module_utils/facts/hardware` — exit 0, 21 passed.
- `git diff --check` — exit 0.

Working tree: modified `lib/ansible/module_utils/facts/hardware/linux.py` and `test/units/module_utils/facts/hardware/test_linux.py`. No offline tooling blockage.
