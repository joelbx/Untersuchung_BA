Implemented normalized author parsing and linked 880 alternate names for 100, 700, and 720 fields in [parse.py](/app/openlibrary/catalog/marc/parse.py). Linked names are deduplicated, and existing organization and event parsing is unchanged. Updated affected parser expectations.

Verification: `pytest -q openlibrary/catalog/marc/tests/test_parse.py` — 59 passed. `git diff --check` passed.