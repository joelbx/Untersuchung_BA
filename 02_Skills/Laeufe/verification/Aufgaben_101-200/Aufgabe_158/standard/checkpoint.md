# Checkpoint

Issue: ZIP archives can report invalid timestamps such as `19800000.000000`; `ZipArchive.is_unarchived` raised `ValueError` while parsing them.

Changes:
- Added regex-based `_valid_time_stamp` to parse `YYYYMMDD.HHMMSS`, enforce ZIP years 1980–2107 and valid calendar values, and return `(1980, 1, 1, 0, 0, 0, 0, 0, 0)` for invalid input.
- `is_unarchived` now uses the sanitized tuple for `time.mktime`.
- Added unit cases for boundaries, leap day, malformed/out-of-range dates, and the original `is_unarchived` failure path.

Verification:
- Red test run before fix: `PYTHONPATH=lib pytest -q test/units/modules/test_unarchive.py` — exit 1, 12 failures including original `ValueError`.
- Final command: `PYTHONPATH=lib python -m compileall -q lib/ansible/modules/unarchive.py test/units/modules/test_unarchive.py && git diff --check && PYTHONPATH=lib pytest -q test/units/modules/test_unarchive.py` — exit 0, 15 passed.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep` instead. No external research or downloads.
