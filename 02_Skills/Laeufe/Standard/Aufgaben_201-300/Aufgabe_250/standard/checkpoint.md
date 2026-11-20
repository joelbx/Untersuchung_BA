# Checkpoint

Task: Add `luqum_replace_child` in `openlibrary/solr/query_utils.py` and verify it with relevant local tests.

Status: Complete. Added `luqum_replace_child` for `BaseOperation`, `Group`, and `Unary`, preserving child order and container type and replacing all equal direct children. Added tests for supported parents, duplicate matches, missing children, and unsupported parents.

Verification: `pytest -q openlibrary/tests/solr/test_query_utils.py` passed (12 tests). `git diff --check` passed. `rg` was unavailable; local searches used `find` and `grep` instead.
