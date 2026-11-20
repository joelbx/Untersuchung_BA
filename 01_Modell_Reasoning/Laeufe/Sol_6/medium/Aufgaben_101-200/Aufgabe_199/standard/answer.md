Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) from `urllib` to `requests`, including status handling, retries, range headers, response content, and text decoding. Updated the dependent MARC subject loader and tests.

Verification: 50 `get_ia` tests passed; `git diff --check` passed.