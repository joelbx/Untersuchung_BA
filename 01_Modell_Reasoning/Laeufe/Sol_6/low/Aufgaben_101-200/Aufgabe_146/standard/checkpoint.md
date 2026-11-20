Task: Add IBM Z / s390 /proc/sysinfo hardware facts fallback in LinuxHardware.
Status: Complete. Added get_sysinfo_facts and applied it during populate. Added absent/present unit tests.
Verification: PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts/hardware/test_linux.py (13 passed).
