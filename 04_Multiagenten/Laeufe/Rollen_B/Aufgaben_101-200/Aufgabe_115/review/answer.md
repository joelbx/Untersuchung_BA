VERDICT: FIX

**Code defects**

- [new_work](/app/openlibrary/catalog/add_book/__init__.py:265) pairs edition author keys with MARC roles by position. The import path can preserve an existing edition’s authors, so equal counts can still assign a role to the wrong person. Match the authors before assigning roles.
- [update_work_with_rec_data](/app/openlibrary/catalog/add_book/__init__.py:911) adds authors to an existing work without their parsed roles. Carry each record author’s role into the work entry.

**Tests:** `python -m pytest -q openlibrary/catalog/marc/tests/test_parse.py openlibrary/catalog/add_book/tests/test_add_book.py` — 162 passed. `python -m pytest -q openlibrary/catalog/add_book/tests/test_load_book.py` — 34 passed.

**TEST_ENVIRONMENT_PROBLEM:** None. This was an independent review; no project code or tests were changed.