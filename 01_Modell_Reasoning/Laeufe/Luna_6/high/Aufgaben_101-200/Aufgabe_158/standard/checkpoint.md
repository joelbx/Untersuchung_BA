# Checkpoint

Task: fix ZIP timestamp handling in the unarchive module.

Implemented `ZipArchive._valid_time_stamp` in `lib/ansible/modules/unarchive.py`. It uses a full-match regular expression to extract the six timestamp components, validates calendar fields and the 1980–2107 ZIP year range, and returns `(1980, 1, 1, 0, 0, 0, 0, 0, 0)` for malformed or out-of-range values. `is_unarchived` now converts the validated tuple with `time.mktime` rather than calling `datetime.datetime` and `time.strptime` itself.

Verification: `pytest -q test/units/modules/test_unarchive.py` passed (3 tests); `git diff --check` passed.
