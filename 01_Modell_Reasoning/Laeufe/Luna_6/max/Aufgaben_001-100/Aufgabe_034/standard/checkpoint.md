# Checkpoint

## Objective
Normalize Internet Archive publisher/place and ISBN metadata in `get_ia_record`, while preserving the existing handling of other edition fields. Add the requested public utilities in `openlibrary/plugins/upstream/utils.py` and verify with relevant existing tests.

## Completed
- Added `get_isbn_10_and_13` and `get_publisher_and_place` to upstream `utils.py`.
- Updated `get_ia_record` to emit `isbn_10`, `isbn_13`, `publishers`, and `publish_places`, omitting empty normalized fields.
- Updated existing import API expectations to match the normalized fields.
- Verified with `pytest openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py`: 17 passed.
- `git diff --check` passed.
