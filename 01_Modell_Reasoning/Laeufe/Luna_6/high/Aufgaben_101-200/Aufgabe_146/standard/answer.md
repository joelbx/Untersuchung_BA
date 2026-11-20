Implemented `/proc/sysinfo` parsing in [linux.py](/app/lib/ansible/module_utils/facts/hardware/linux.py:314). It returns the five required facts, defaults missing values to `"NA"`, strips leading zeros from the serial, and fills DMI facts that are unavailable.

Validation passed: `test_linux.py` (11 tests) and `git diff --check`.