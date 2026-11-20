Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) from urllib to `requests`, including status handling, UTF-8 fallback, response content, and Range headers. Updated the [MARC subject caller](/app/openlibrary/catalog/marc/marc_subject.py) and [tests](/app/openlibrary/tests/catalog/test_get_ia.py).

Verification: 166 relevant tests passed, and `git diff --check` passed.