Task: Fix book import cover URL validation for allowed hosts.
Status: Complete.
Changes: Added ALLOWED_COVER_HOSTS and process_cover_url; new and matched edition imports now discard unsupported cover URLs before upload. Added helper and import-path tests.
Verification: pytest -q openlibrary/catalog/add_book/tests/test_add_book.py (89 passed); ruff check passed; git diff --check passed.
