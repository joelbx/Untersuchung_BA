Moved edition expansion to [catalog/utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py) as `expand_record()`, updated the `add_book` callers and tests, and removed `build_marc()` from `merge_marc.py`. The title helper remains importable from its old location for compatibility.

Verification: 85 tests passed, 8 skipped, and 2 expected failures. Ruff and `git diff --check` passed.