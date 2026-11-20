Updated [vendors.py](/app/openlibrary/core/vendors.py): Amazon edition language display values are included when present, with “Original Language” entries filtered out and duplicates removed. The metadata cleaner now preserves `languages`.

Verification: `pytest -q openlibrary/tests/core/test_vendors.py` passed (33 tests); `git diff --check` passed.