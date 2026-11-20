Implemented cover host filtering in [add_book/__init__.py](/app/openlibrary/catalog/add_book/__init__.py:79). `process_cover_url` removes the `cover` key and returns its URL only when the hostname matches `ALLOWED_COVER_HOSTS`, case-insensitively, over HTTP or HTTPS. Both new and matched edition import paths use it.

Updated the matched-cover fixture to use an allowed host in [test_add_book.py](/app/openlibrary/catalog/add_book/tests/test_add_book.py:1184).

Verification: `pytest -q openlibrary/catalog/add_book/tests` — **140 passed, 1 xfailed**. `git diff --check` passed.