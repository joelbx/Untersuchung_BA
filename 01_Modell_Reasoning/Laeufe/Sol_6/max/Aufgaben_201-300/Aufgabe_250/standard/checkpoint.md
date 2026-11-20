Task: Add `luqum_replace_child` in `openlibrary/solr/query_utils.py`.

Status: Implemented the helper for `BaseOperation`, `Group`, and `Unary` parents. It preserves the child sequence type and order, replaces all equal direct children, leaves a missing child untouched, and raises the existing `ValueError` for unsupported parents.

Verification: `pytest -q openlibrary/tests/solr/test_query_utils.py` passed (12 tests). `git diff --check` passed. The `black` executable is unavailable in this environment.
