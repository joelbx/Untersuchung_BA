# Checkpoint

Task: Refactor `build_marc()` into public `catalog.utils.expand_record()` and update callers/docs/tests.

Completed: Moved title expansion to `catalog.utils.build_titles()`, added `expand_record()`, removed `build_marc()` from merge code, updated add_book callers and relevant tests/comments. A repository search found no remaining `build_marc` references.

Verification: `pytest -q openlibrary/catalog/merge/tests/test_merge_marc.py openlibrary/catalog/add_book/tests/test_match.py openlibrary/tests/catalog/test_utils.py` — 21 passed, 2 xfailed.
