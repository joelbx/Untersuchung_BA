# Checkpoint

Implemented `LinuxHardware.get_sysinfo_facts` in `lib/ansible/module_utils/facts/hardware/linux.py` and merged its results into the DMI facts during hardware collection. The method returns `{}` without `/proc/sysinfo`; otherwise it returns the five required fields, defaults undiscovered values to `NA`, parses Manufacturer/Type/Sequence Code, and strips leading serial zeros.

Validation: `python -m pytest test/units/module_utils/facts/hardware/test_linux.py -q` passed (11 tests). `git diff --check` passed.
