Added `STAGED_SOURCES = ('amazon', 'idb')` and `ImportItem.find_staged_or_pending` in [imports.py](/app/openlibrary/core/imports.py). The method builds `{source}:{identifier}` IDs and returns matching staged or pending rows from `import_item`.

Added coverage in [test_imports.py](/app/openlibrary/tests/core/test_imports.py). All 6 tests in that file pass.