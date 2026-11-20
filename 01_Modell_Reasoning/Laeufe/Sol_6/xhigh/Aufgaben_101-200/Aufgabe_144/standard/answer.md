Moved edition expansion to [catalog utils](/app/openlibrary/catalog/utils/__init__.py) as `expand_record()`, moved its title helper alongside it, and updated the add_book callers, documentation, and tests. The old `build_marc()` function is removed.

Verification: 99 catalog tests passed; 8 skipped and 2 expected failures.