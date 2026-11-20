Updated [aix.py](/app/lib/ansible/module_utils/facts/hardware/aix.py) to report processor count as 1, count available processor devices as cores, default threads per core to 1, calculate vCPUs, and return the CPU type in a list.

Verification passed: 106 existing tests passed and 5 were skipped. Mocked AIX checks covered reported and default SMT values; `git diff --check` passed.