Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) from `urllib` to `requests`, including status checks, response content handling, UTF-8 fallback, and Range headers. Updated its dependent caller in [marc_subject.py](/app/openlibrary/catalog/marc/marc_subject.py).

Verification: 45 `get_ia` tests passed; `git diff --check` passed.