Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) to `requests`, including status validation, retries, range headers, and response content handling. Updated the existing test fixture to return a `requests.Response`.

Verification: `pytest -q openlibrary/tests/catalog/test_get_ia.py` passed (42 tests); `git diff --check` passed.