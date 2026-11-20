# Checkpoint

Implemented `luqum_replace_child` in `openlibrary/solr/query_utils.py`. It accepts `BaseOperation`, `Group`, and `Unary` parents, rebuilds the existing children sequence type while substituting all children equal to `old_child`, and leaves the parent unchanged when there is no match. Unsupported parent types raise `ValueError("Not supported for generic class Item")`.

Added focused tests in `openlibrary/tests/solr/test_query_utils.py` for replacement, tuple preservation, missing child behavior, and unsupported parents.

Verification: `python -m pytest openlibrary/tests/solr/test_query_utils.py -q` passed (9 tests).
