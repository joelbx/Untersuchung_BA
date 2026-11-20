Updated the AIX hardware collector so `processor_count` is 1, `processor_cores` counts available processor devices, SMT supplies `processor_threads_per_core` with a default of 1, and `processor_vcpus` is their product. `processor` is now a list.

Added AIX unit tests. The hardware fact test suite passed: **17 tests**.