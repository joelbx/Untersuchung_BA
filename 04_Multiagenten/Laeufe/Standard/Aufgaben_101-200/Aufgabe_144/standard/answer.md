Moved edition expansion to [catalog utils](/app/openlibrary/catalog/utils/__init__.py) as `expand_record`, alongside its title helper. Updated the `add_book` callers and tests, and removed `build_marc` from `merge_marc.py`.

Verification: 84 catalog tests passed, 8 skipped, 2 expected failures. Ruff and `git diff --check` passed.