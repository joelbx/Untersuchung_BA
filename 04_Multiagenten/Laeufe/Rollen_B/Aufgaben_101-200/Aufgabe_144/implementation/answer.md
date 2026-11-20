Moved edition expansion to [`expand_record()`](/app/openlibrary/catalog/utils/__init__.py) and placed its title expansion helper alongside it. Updated the `add_book` callers, documentation, and tests, and removed `build_marc`.

Validation: 85 tests passed, 8 skipped, and 2 had expected failures. Ruff and `git diff --check` passed.