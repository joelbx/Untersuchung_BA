Implemented `/proc/sysinfo` support in [linux.py](/app/lib/ansible/module_utils/facts/hardware/linux.py:414). When the file exists, `get_sysinfo_facts` returns the five required fields, defaults missing values to `"NA"`, and strips leading zeros from `Sequence Code`. Its values are merged into the hardware facts.

Validation passed: `test_linux.py` (11 tests) and `git diff --check`.