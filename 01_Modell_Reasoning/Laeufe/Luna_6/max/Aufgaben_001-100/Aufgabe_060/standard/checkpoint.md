# Checkpoint

Task: Resolve author import matching with Open Library keys and external remote identifiers.

Completed:
- Added `AuthorRemoteIdConflictError` and `Author.merge_remote_ids`, which preserves new IDs, counts exact matches, and rejects value conflicts.
- Author imports now match by Open Library key first, then exact remote IDs, then existing name/date rules. Remote-ID candidates are ranked by overlap and stable OLID/key ordering.
- New author candidates retain supplied remote IDs. Changed remote IDs on matched authors are included in the save edits.
- Added the `wikisource` exemption from suspect-date removal.

Verification: `pytest -q openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/tests/core/test_models.py` passed (141 tests). `git diff --check` and `compileall` also passed.
