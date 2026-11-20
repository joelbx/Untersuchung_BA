Updated [aix.py](/app/lib/ansible/module_utils/facts/hardware/aix.py:59) to report processor count as `1`, count available processor devices as cores, default threads per core to `1`, calculate vCPUs, and return the CPU type in a list.

Validation: the existing hardware facts suite passed (15 tests), and `git diff --check` passed. There is no AIX-specific unit test in that suite.