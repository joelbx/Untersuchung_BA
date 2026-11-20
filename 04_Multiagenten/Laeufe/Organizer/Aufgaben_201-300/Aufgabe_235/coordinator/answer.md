Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) so person authors from MARC 100, 700, and 720 include deduplicated names from linked 880 fields. Added `name_from_list` for name normalization and updated the relevant fixtures and tests. Organization and event parsing remains unchanged.

**Verification:** `pytest -q openlibrary/catalog/marc/tests` — 124 passed. No delegation was used.