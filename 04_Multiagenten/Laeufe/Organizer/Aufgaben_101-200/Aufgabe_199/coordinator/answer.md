Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) from `urllib` to `requests`, including response content, text decoding, HTTP error handling, and Range headers. Updated the dependent [marc_subject.py](/app/openlibrary/catalog/marc/marc_subject.py) callers and added focused tests.

The relevant test suites passed: **95 tests**. No delegation was used.