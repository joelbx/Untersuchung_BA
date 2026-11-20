Fixed ZIP timestamp handling in [unarchive.py](/app/lib/ansible/modules/unarchive.py). The new `_valid_time_stamp` method validates the date and ZIP year range, then uses the required 1980 epoch for invalid timestamps such as `19800000.000000`.

Added regression coverage in [test_unarchive.py](/app/test/units/modules/test_unarchive.py). The unarchive unit suite passed: **16 tests**.