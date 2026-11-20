Added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending` in [imports.py](/app/openlibrary/core/imports.py). The lookup returns staged or pending `import_item` rows for source-prefixed identifiers. [ISBN resolution](/app/openlibrary/core/models.py) now uses it for both ISBN-13 and ISBN-10.

Verification: all 6 tests in `test_imports.py` pass, and `git diff --check` passes.