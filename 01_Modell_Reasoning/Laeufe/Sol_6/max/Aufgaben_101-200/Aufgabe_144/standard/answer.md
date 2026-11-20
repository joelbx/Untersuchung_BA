Moved record expansion to [catalog.utils.expand_record](/app/openlibrary/catalog/utils/__init__.py:75), including its title helper. Updated `add_book` matching, removed `build_marc` from `merge_marc.py`, and moved and expanded the relevant tests.

Verification: 89 tests passed; 3 had expected failures and 8 were skipped. Ruff and `git diff --check` passed.