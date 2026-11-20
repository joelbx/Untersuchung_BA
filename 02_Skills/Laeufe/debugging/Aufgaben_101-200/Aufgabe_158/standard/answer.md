Fixed the unarchive crash for ZIP entries with invalid timestamps. `ZipArchive._valid_time_stamp` now validates the date and uses the 1980 ZIP epoch when it is invalid, so `is_unarchived` can continue processing the entry.

The regression test reproduced the reported `ValueError` before the fix. After the fix, all 13 unarchive unit tests pass, and `git diff --check` passes.