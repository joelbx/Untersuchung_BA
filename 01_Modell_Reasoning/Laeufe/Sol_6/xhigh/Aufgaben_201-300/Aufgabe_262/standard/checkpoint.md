Task: Fix book imports so cover URLs are fetched only from allowed hosts.
Status: Implemented `ALLOWED_COVER_HOSTS` and `process_cover_url`; new and matched edition imports now validate and remove cover URLs before upload.
Verification: `pytest -q openlibrary/catalog/add_book/tests` (152 passed, 1 xfailed); Ruff check passed; `git diff --check` passed.
