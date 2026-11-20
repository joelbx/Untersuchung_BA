Task: Fix s390 Linux hardware facts using /proc/sysinfo.
Status: Complete.
Changes: Added LinuxHardware.get_sysinfo_facts and merged its five identity fields into DMI facts. Added unit tests for absent, partial, and complete sysinfo and DMI fallback integration.
Validation: PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts/hardware (21 passed); git diff --check passed.
