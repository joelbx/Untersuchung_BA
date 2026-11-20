Updated [aix.py](/app/lib/ansible/module_utils/facts/hardware/aix.py) so AIX reports available processor devices as cores, fixes `processor_count` at 1, defaults threads per core to 1, derives virtual CPUs, and returns the CPU type as a list.

Validation passed: 15 existing hardware facts unit tests, `py_compile`, and `git diff --check`. There are no AIX-specific tests in that test directory.