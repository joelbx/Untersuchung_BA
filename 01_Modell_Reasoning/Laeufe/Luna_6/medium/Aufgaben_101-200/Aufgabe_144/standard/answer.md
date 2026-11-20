Implemented `expand_record()` in [catalog/utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py). Title expansion now lives in `catalog.utils`, and `build_marc()` has been removed from `merge_marc.py`.

Updated add_book callers, comparison documentation, and existing test references. Focused tests passed: **8 passed, 2 xfailed**.