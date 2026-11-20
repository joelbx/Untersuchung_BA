# Checkpoint

Task: Add a local lookup for staged or pending import items by source-prefixed identifiers in `openlibrary/core/imports.py`.

Completed: added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending` to query local `import_item` rows with staged or pending status. Updated `Edition.from_isbn` to use the helper with both ISBN-13 and ISBN-10, and to check both identifiers when looking for the imported edition. Added focused lookup and ISBN resolution tests.

Verification: `python -m pytest -q openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py` (20 passed); `python -m ruff check` on changed Python files (passed); `git diff --check` (passed).
