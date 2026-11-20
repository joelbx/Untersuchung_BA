Added `STAGED_SOURCES = ('amazon', 'idb')` and [ImportItem.find_staged_or_pending](/app/openlibrary/core/imports.py:125). It returns all matching staged or pending `import_item` rows as a database result set.

[Edition.from_isbn](/app/openlibrary/core/models.py:373) now uses the local lookup for both ISBN-13 and ISBN-10 records. Verification passed: 20 relevant tests, Ruff, and `git diff --check`.