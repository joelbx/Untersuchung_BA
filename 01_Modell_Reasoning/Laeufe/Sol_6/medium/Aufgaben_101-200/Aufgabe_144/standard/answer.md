Moved edition expansion to `expand_record()` in [catalog.utils](/app/openlibrary/catalog/utils/__init__.py), alongside its title expansion helper. Updated the add book callers and tests, and removed `build_marc()` from `merge_marc.py`.

Verification: the broader catalog suite had 84 passed, 8 skipped, and 2 expected failures. Focused tests, Ruff, and `git diff --check` also passed.