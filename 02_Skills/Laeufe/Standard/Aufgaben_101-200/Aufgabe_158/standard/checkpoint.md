# Checkpoint

Task: fix invalid ZIP timestamps in unarchive.

Implemented `ZipArchive._valid_time_stamp` with regex extraction, ZIP year bounds (1980–2107), date and clock validation, and the specified ZIP epoch fallback. `is_unarchived` now uses the sanitized time tuple before `time.mktime`.

Added unit coverage for boundary dates, malformed timestamps, invalid calendar values, and the reported timestamp with an existing destination file.

Checks run:
- `python -m pytest -q test/units/modules/test_unarchive.py` — 13 passed.
- `git diff --check` — passed.
