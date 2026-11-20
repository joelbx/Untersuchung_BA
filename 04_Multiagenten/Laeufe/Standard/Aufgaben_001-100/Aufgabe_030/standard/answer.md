Updated the AIX hardware facts collector to report `processor_count` as 1, count available processor devices as cores, default threads per core to 1, derive vCPUs, and return the CPU type as a list. Added tests for reported SMT threads, missing SMT data, and no available processors.

Verification: all 18 hardware facts unit tests passed, and `git diff --check` passed.