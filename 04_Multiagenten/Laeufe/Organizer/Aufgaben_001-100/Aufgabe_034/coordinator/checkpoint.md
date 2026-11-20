Task: Normalize IA publisher/place and ISBN metadata in get_ia_record.
Status: Complete. Implemented public upstream utilities and wired them into the IA importer. Updated existing expectations and added mixed/empty input coverage.
Verification: pytest -q openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py (24 passed); pytest -q openlibrary/plugins/importapi/tests (14 passed); git diff --check passed.
Delegation: None; solved directly.
