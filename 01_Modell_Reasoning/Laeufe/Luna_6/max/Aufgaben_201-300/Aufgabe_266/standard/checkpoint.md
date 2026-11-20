# Checkpoint

## Task
Implement `find_staged_or_pending` in `openlibrary/core/imports.py` so ISBN/identifier lookups can retrieve local staged or pending `import_item` rows for fixed source prefixes including `amazon` and `idb`.

## Progress
- Inspected `ImportItem` and `Edition.from_isbn`; the ISBN resolver had an inline query for the same staged/pending source IDs.
- Added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending`, then routed `Edition.from_isbn` through the helper.
- Reviewed the diff; `git diff --check` is clean.
- Ran `python -m pytest openlibrary/tests/core/test_imports.py`: 5 passed.
