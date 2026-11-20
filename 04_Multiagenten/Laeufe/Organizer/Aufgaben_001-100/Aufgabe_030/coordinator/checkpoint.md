Issue: AIX hardware processor facts mapped incorrectly.
Completed: set processor_count to 1, count Available devices as processor_cores, return CPU type as a list, default SMT to 1, and compute processor_vcpus. Added AIX CPU regression tests for reported SMT, missing SMT, and no Available device.
Verification: python -m pytest -q test/units/module_utils/facts/hardware (18 passed); AIX fact platform selection tests (9 selected passed); git diff --check passed.
Delegation: none.
