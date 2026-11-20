Updated the AIX hardware facts collector to report `processor_count` as 1, count available processor devices as cores, default threads per core to 1, calculate vCPUs, and return the CPU type as a list. Added tests for reported and missing SMT values and for no available processors.

The hardware facts test suite passed: **18 tests**.