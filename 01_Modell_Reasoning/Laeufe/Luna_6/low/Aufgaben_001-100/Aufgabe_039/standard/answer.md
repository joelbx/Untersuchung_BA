Fixed work ID conflicts so failed updates preserve the source row and report the failure in the returned count dictionary. Updated the admin summary and added regression coverage.

Validation passed: `python -m pytest openlibrary/tests/core/test_db.py -q` (3 tests) and `git diff --check`.