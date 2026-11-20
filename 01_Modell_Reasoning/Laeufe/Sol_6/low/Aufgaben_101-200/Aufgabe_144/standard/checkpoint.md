Task: relocate build_marc to catalog.utils.expand_record and update callers.
Status: complete.
Changed: moved build_titles and expansion into catalog.utils; updated add_book, merge docs, and tests.
Verification: pytest -q openlibrary/catalog/merge/tests openlibrary/catalog/add_book/tests: 84 passed, 8 skipped, 2 xfailed. git diff --check passed.
