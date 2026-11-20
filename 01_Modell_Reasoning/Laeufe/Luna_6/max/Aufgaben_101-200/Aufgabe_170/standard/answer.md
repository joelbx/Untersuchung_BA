Implemented the edition matching fixes.

- Added `add_db_name`, `expand_record`, and `threshold_match` in [merge_marc.py](/app/openlibrary/catalog/merge/merge_marc.py:88). `editions_match` now accepts raw or expanded records, handles missing fields, and compares authors across author/contributor roles, including reordered names.
- Kept the `catalog.utils` expansion functions compatible through delegating wrappers in [utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py:298).
- Promoted the formerly xfailed full-edition match to a regular test in [test_match.py](/app/openlibrary/catalog/add_book/tests/test_match.py:20).

Verification: **10 passed, 1 unrelated xfailed**. Ruff and `git diff --check` passed.