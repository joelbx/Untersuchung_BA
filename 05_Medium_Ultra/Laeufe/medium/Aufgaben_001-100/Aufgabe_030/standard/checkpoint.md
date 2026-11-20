Task: Correct AIX processor facts in the checked-out repository.
Status: Implemented AIX processor fact corrections and added unit coverage for reported SMT and missing SMT.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/facts/hardware (17 passed); git diff --check passed.
