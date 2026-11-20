Updated [AIX hardware facts](/app/lib/ansible/module_utils/facts/hardware/aix.py) to report one processor, count available devices as cores, use the reported SMT threads or default to one, derive vCPUs, and return the CPU type as a list.

Added [focused tests](/app/test/units/module_utils/facts/hardware/test_aix_get_cpu_facts.py). All 9 relevant tests passed, and `git diff --check` passed.