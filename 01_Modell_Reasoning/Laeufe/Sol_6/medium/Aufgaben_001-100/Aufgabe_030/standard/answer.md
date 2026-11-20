Updated the [AIX hardware fact collector](/app/lib/ansible/module_utils/facts/hardware/aix.py) to report `processor_count` as `1`, count available devices as cores, use reported SMT threads or default to `1`, calculate vCPUs, and return the CPU type in a list. Added [regression tests](/app/test/units/module_utils/facts/hardware/test_aix_get_cpu_facts.py).

All 18 hardware fact unit tests pass.