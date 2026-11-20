Task: Fix unarchive handling of invalid ZIP timestamps.
Status: Implemented ZIP timestamp validation and fallback to the ZIP epoch. Added unit coverage for date bounds, malformed dates, and the reported failure in is_unarchived.
Verification: python -m pytest -q test/units/modules/test_unarchive.py (13 passed); git diff --check passed.
