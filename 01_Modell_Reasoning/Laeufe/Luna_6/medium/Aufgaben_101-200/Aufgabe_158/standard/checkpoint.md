Task: Fix unarchive ZIP timestamp parsing failures.

Implemented ZipArchive._valid_time_stamp with regex parsing, valid ZIP year bounds (1980–2107), calendar/time validation, and the required epoch fallback tuple. is_unarchived now uses the sanitizer before mktime. Added unit coverage for valid leap dates, malformed dates, out-of-range years, and malformed strings.

Verification: python -m pytest test/units/modules/test_unarchive.py -q (9 passed); git diff --check passed.
