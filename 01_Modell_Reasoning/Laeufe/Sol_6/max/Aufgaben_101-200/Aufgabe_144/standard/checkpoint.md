# Checkpoint

Task: move `build_marc` record expansion to public `catalog.utils.expand_record`, update callers and documentation, and verify with existing repository tests.

Status: implementation complete. `expand_record` and its title helper now live in `catalog.utils`; `add_book`, matching, docs, and tests use the new interface. `build_marc` is removed from `merge_marc.py`.

Verification: 53 passed, 2 expected failures in focused matching and add_book tests; 36 passed, 8 skipped, 1 expected failure in the remaining merge and load_book tests. Ruff passed on changed Python files. External research was unavailable; repository files and existing tests were the sources of truth.
