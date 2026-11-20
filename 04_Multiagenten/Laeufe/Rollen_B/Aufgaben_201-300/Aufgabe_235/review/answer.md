VERDICT: FIX

**Code defect:** [name_from_list](/app/openlibrary/catalog/marc/parse.py:383) calls `strip_foc` before removing a terminal period. For a MARC 100 name of `Smith [from old catalog].`, `read_author_person` stores `Smith [from old catalog` in both `name` and `personal_name`. The new interface requires the marker to be removed. Strip terminal punctuation before the marker, or make marker removal accept the period.

**Tests run:** `pytest -q openlibrary/catalog/marc/tests/test_parse.py` — 61 passed; `pytest -q openlibrary/catalog/marc/tests` — 122 passed. No TEST_ENVIRONMENT_PROBLEM.