# Checkpoint

Implemented `luqum_replace_child` in `openlibrary/solr/query_utils.py`. It supports `BaseOperation`, `Group`, and `Unary`, rebuilds the children tuple in order, replaces all equal matching children, leaves unmatched children semantically unchanged, and uses the required `ValueError` message for unsupported parents.

Verification:
- `pytest -q openlibrary/tests/solr/test_query_utils.py`: 6 passed.
- Direct runtime assertions covered replacement, tuple/order preservation, absent child, and unsupported parent error.
- `git diff --check`: passed.
