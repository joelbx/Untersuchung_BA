Replaced urllib HTTP calls in [get_ia.py](/app/openlibrary/catalog/get_ia.py) with `requests`, including status handling, retries, UTF-8 fallback, and response content access. Updated the dependent MARC subject helpers and added focused tests.

Validation: 95 relevant tests passed; `git diff --check` passed.