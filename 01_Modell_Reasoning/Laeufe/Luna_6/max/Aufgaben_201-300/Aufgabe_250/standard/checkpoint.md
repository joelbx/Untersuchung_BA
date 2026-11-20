# Checkpoint

Task: implement `luqum_replace_child` in `openlibrary/solr/query_utils.py` per the issue.

Completed: the helper rejects unsupported parent types with the existing `ValueError` message, substitutes all equal direct children, preserves the children sequence type and order, and leaves the sequence untouched when there is no match.

Verification: `pytest -q openlibrary/tests/solr/test_query_utils.py` passed (6 tests).
