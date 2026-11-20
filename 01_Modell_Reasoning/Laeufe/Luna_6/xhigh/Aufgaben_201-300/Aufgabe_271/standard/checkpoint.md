# Checkpoint

Issue: Fix Internet Archive publisher and ISBN metadata handling in ImportAPI.

Changes made:
- Added `get_colon_only_loc_pub` and `get_location_and_publisher` with ordered place/publisher parsing, bracket cleanup for parsed fields, unidentified-place handling, comma fallback, and malformed multi-colon handling.
- Updated IA record construction to always represent provided publisher metadata as a list and split location-bearing strings through the new location-first helper.
- Moved `get_isbn_10_and_13` into `openlibrary.utils.isbn`; ImportAPI imports it there. Kept upstream compatibility exports for existing code/tests.

Verification: `pytest -q openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py openlibrary/utils/tests/test_isbn.py` passed (35 tests). `git diff --check` passed.
