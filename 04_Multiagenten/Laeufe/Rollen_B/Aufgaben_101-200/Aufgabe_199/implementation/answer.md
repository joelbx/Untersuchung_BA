Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) from urllib to `requests`, including response handling, retries, range headers, XML parsing, and UTF-8 fallback. Updated its deprecated consumer and the response mocks in the tests.

Verification: all 50 focused tests pass, and `git diff --check` is clean.