Task: Add `luqum_replace_child` to `openlibrary/solr/query_utils.py` and verify it with existing Luqum tests.

Completed: Added `luqum_replace_child` for BaseOperation, Group, and Unary nodes. It preserves the children sequence type and order, replaces all equal direct children, leaves missing children untouched, and raises the existing ValueError for unsupported parents.

Verification: `python -m pytest openlibrary/tests/solr -q` passed (85 tests). `git diff --check` passed. Black is unavailable in the environment.
