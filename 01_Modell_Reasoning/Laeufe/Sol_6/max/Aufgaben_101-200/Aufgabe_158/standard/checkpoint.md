# Unarchive ZIP timestamp fix

Status: fixed and verified.

Changes: `ZipArchive._valid_time_stamp` parses YYYYMMDD.HHMMSS with a regular expression, accepts ZIP years 1980 through 2107, validates calendar fields, and falls back to the 1980-01-01 ZIP epoch for invalid values. `is_unarchived` now uses it for timestamp comparison. Added focused unit coverage, including the reported `19800000.000000` value on an existing destination file.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/modules/test_unarchive.py` (15 passed); `git diff --check` (passed).

Constraints: edit checked-out files only; use local code and tests; preserve git history and index.
