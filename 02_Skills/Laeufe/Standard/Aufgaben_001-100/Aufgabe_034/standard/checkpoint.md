# Checkpoint

Task: Normalize IA publisher/place and ISBN fields in `get_ia_record` via public upstream utilities.

Completed:
- Added `get_isbn_10_and_13` and `get_publisher_and_place` to `openlibrary.plugins.upstream.utils`.
- Updated IA import to emit normalized edition fields and omit empty normalized fields.
- Updated and added tests for string, list, mixed, whitespace, invalid, and empty inputs.

Checks:
- `pytest -q openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py` — 29 passed.
- `pytest -q openlibrary/plugins/importapi/tests` — 17 passed.
- `git diff --check` — passed.

Notes: `rg` was unavailable, so repository search used `grep` and `find`. No offline checks were blocked.
