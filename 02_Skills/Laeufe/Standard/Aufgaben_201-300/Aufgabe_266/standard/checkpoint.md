# Checkpoint

Implemented `STAGED_SOURCES = ('amazon', 'idb')` and `ImportItem.find_staged_or_pending(identifiers, sources=STAGED_SOURCES)` in `openlibrary/core/imports.py`. The method forms every `{source}:{identifier}` pair and queries staged or pending `import_item` rows. Empty inputs return an empty database result set.

Updated `Edition.from_isbn` to use this lookup with ISBN 13 and ISBN 10, and to check both ISBN forms when looking for the imported edition. Added focused tests for the lookup, source override, status filtering, empty identifiers, and ISBN 10 resolution.

Checks: `python -m pytest openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py -q --override-ini reruns=0` passed (17 tests). `git diff --check` and `python -m ruff check openlibrary/core/imports.py openlibrary/core/models.py openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py` passed. An initial focused test failed because SQLite returns `SqliteResultSet` rather than `ResultSet`; the test now asserts the SQLite result type and the final run passes.
