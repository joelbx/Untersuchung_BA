VERDICT: FIX

**Code defect:** [expand_record](/app/openlibrary/catalog/merge/merge_marc.py:91) overwrites existing author and contributor `db_name` values. I reproduced a false negative at threshold 875: two records with the same `db_name`, title, and year but different display names returned `False`. Preserve supplied `db_name` values and add a cross-role regression case.

**Tests executed:** `python -m pytest -q openlibrary/catalog/merge/tests/test_merge_marc.py openlibrary/catalog/add_book/tests/test_match.py` — 12 passed, 1 xfailed; `python -m pytest -q openlibrary/catalog/add_book/tests/test_add_book.py` — 63 passed; `python -m pytest -q openlibrary/tests/catalog/test_utils.py` — 57 passed. `git diff --check` passed. **TEST_ENVIRONMENT_PROBLEM:** none.