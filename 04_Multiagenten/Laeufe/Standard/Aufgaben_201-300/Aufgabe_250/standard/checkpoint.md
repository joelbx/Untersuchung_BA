Task: Add luqum_replace_child in openlibrary/solr/query_utils.py.
Status: Complete.
Changes: Supported BaseOperation, Group, and Unary; replace all equal direct children while preserving sequence type and order; leave absent matches unchanged; raise the existing ValueError for unsupported parents. Added focused tests.
Verification: pytest -q openlibrary/tests/solr/test_query_utils.py (12 passed); git diff --check passed.
