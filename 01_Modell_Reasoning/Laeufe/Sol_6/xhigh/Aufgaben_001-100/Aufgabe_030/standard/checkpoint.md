Task: Fix AIX processor facts in the checked-out repository.
Status: Complete.
Changes: AIX processor_count is 1; processor_cores counts available processor devices; processor_threads_per_core defaults to 1 or uses the reported SMT value; processor_vcpus is their product; processor is a list of the CPU type. Added focused AIX regression tests.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/facts/hardware/test_aix.py test/units/module_utils/facts/test_facts.py::TestAIXHardware (6 passed). git diff --check passed.
