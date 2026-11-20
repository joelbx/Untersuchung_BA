# Checkpoint

Implemented `catalog.utils.expand_record()` and relocated title variant generation to `catalog.utils.build_titles()`. Removed `build_marc()` from `merge_marc.py`, updated add_book callers, comparison documentation, and existing focused test references.

Verification: `python -m pytest openlibrary/catalog/merge/tests/test_merge_marc.py openlibrary/catalog/add_book/tests/test_match.py -q` — 8 passed, 2 xfailed.
