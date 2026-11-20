Updated the AIX hardware collector to report one processor, count available cores from `lsdev`, default threads per core to 1, calculate vCPUs, and return the CPU type as a list.

Added tests for reported and missing thread counts. Both pass: `python -m pytest -q test/units/module_utils/facts/hardware/test_aix.py`.