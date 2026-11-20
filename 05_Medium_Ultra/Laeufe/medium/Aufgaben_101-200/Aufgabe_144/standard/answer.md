Moved edition expansion to [catalog utils](/app/openlibrary/catalog/utils/__init__.py) as `expand_record()`, including the title helper it depends on. Updated add_book matching, comments, and tests to use it, and removed `build_marc()` from `merge_marc.py`.

Verification: 85 tests passed, 8 skipped, 2 expected failures. Ruff and `git diff --check` passed.