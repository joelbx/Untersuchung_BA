VERDICT: FIX
Review complete. Relevant existing tests executed:
- python -m pytest -q openlibrary/catalog/marc/tests/test_parse.py openlibrary/catalog/add_book/tests/test_add_book.py — 162 passed.
- python -m pytest -q openlibrary/catalog/add_book/tests/test_load_book.py — 34 passed.
CODE DEFECTS:
- openlibrary/catalog/add_book/__init__.py:265 pairs preserved edition author keys with current record roles by position. load_data at lines 606-608 preserves existing edition authors, so a new work can assign a MARC role to the wrong person when names/order differ, even if counts match. Align authors by identity, or preserve original matching role associations.
- openlibrary/catalog/add_book/__init__.py:911-917 adds authors to an existing work without any role field. Use the original record author role when constructing these entries.
TEST_ENVIRONMENT_PROBLEM: None.
No project code or tests changed during review.
