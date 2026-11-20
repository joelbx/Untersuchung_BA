# Checkpoint

Task: Resolve author matching issues involving honorifics, names with asterisks, and date formats.

Initial inspection: `rg` is unavailable in this environment. Located matching code in `openlibrary/catalog/add_book/load_book.py`, date extraction in `openlibrary/core/helpers.py`, and year comparison in `openlibrary/catalog/utils/__init__.py`.

Implementation progress: Updated author lookups to escape literal asterisks, compare extracted years, and use surname queries only when both years are present. Updated honorific removal to accept and return a string, preserve honorific-only names, and honor punctuation-insensitive exceptions. `build_query` now cleans copied author records before importing them.

Validation: Direct helper checks passed and `git diff --check` passed. Existing `test_load_book.py` has 17 passing tests and 11 failures tied to old dictionary-API and wildcard-as-pattern expectations. Existing `test_match.py` has 28 passing, 1 xfailed, and 1 unrelated failure in `test_editions_match_identical_record`.
