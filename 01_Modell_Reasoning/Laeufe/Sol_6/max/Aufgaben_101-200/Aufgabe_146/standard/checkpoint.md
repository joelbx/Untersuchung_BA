Task: Fix s390 hardware facts in lib/ansible/module_utils/facts/hardware/linux.py.
Status: Complete. Added get_sysinfo_facts and integrated it into LinuxHardware.populate so /proc/sysinfo values override DMI NA values. Added tests for absent, complete, partial, and gathered facts.
Verification: PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts/hardware (21 passed); git diff --check passed.
Changed tracked files: lib/ansible/module_utils/facts/hardware/linux.py; test/units/module_utils/facts/hardware/test_linux.py.
