Fixed the ZIP timestamp crash in [unarchive.py](/app/lib/ansible/modules/unarchive.py). The new `_valid_time_stamp` method validates the date fields and uses the ZIP epoch for invalid values such as `19800000.000000`. Added regression coverage in [test_unarchive.py](/app/test/units/modules/test_unarchive.py).

Verification: all 20 unarchive unit tests pass; `git diff --check` passes.