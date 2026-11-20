# Checkpoint

Completed the move to `openlibrary.catalog.utils.expand_record`, moved title expansion alongside it, updated all add-book callers and merge documentation, and migrated the existing tests. Added assertions for merged ISBNs, optional copied fields, and placeholder country filtering.

Verification: `pytest -q openlibrary/catalog/merge/tests/test_merge_marc.py openlibrary/catalog/add_book/tests/test_match.py` passed (8 passed, 2 expected xfails). `git diff --check` passed. No `build_marc` references remain in `openlibrary/`.
