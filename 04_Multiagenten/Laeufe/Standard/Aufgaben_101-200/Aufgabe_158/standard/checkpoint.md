Task: Fix unarchive ZIP timestamp parsing for invalid ZIP dates.

Status: Implemented ZipArchive._valid_time_stamp with regex parsing, ZIP year bounds, calendar/time validation, and ZIP epoch fallback. is_unarchived now uses it. Added unit coverage for timestamp edge cases and an existing-file regression case.

Verification: python -m pytest -q test/units/modules/test_unarchive.py (15 passed); git diff --check (passed).

Constraints: Use local code and existing tests only; do not change git history, index, or harness configuration.
