# Checkpoint

- Objective completed: added staged and pending import lookup for the fixed `amazon` and `idb` source tuple.
- `ImportItem.find_staged_or_pending` builds each `{source}:{identifier}` value, accepts any iterable of sources, returns matching rows from `import_item`, and returns an empty result when no IDs are generated.
- `Edition.from_isbn` now uses the helper before processing a matching local import item.
- Added test coverage for default sources, custom source iterators, staged/pending filtering, and empty generated IDs.
- Verification passed: `pytest -q openlibrary/tests/core/test_imports.py` (8 passed), `pytest -q openlibrary/tests/core/test_models.py` (10 passed), `ruff check` on changed Python files, and `git diff --check`.
