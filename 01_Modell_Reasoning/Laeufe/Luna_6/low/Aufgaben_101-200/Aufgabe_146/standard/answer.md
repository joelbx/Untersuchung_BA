Implemented `/proc/sysinfo` support in [linux.py](/app/lib/ansible/module_utils/facts/hardware/linux.py:411). When the file exists, the new method returns the five required facts, fills absent values with `"NA"`, and strips leading zeros from the sequence code. The results are merged into DMI facts.

Focused existing tests passed: `11 passed` in `test_linux.py`.