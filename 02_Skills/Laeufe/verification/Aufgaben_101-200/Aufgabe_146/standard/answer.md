Updated [linux.py](/app/lib/ansible/module_utils/facts/hardware/linux.py) to read IBM Z identity facts from `/proc/sysinfo` and include them in setup facts. Added coverage in [test_linux.py](/app/test/units/module_utils/facts/hardware/test_linux.py).

Verification: all 21 hardware unit tests passed, and `git diff --check` passed.