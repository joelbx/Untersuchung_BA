Implemented ZIP timestamp validation in [unarchive.py](/app/lib/ansible/modules/unarchive.py:301). It extracts and validates timestamp components, accepts years 1980–2107, and falls back to the ZIP epoch for malformed or invalid dates. `is_unarchived` now uses this validator.

Added unit coverage for valid timestamps, malformed input, and out-of-range years in [test_unarchive.py](/app/test/units/modules/test_unarchive.py:21).

Verification: `python -m pytest -q test/units/modules/test_unarchive.py` passed (9 tests); `git diff --check` passed.