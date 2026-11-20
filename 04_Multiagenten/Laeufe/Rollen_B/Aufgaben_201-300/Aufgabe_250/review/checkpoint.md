VERDICT: ACCEPT
Reviewed openlibrary/solr/query_utils.py and openlibrary/tests/solr/test_query_utils.py. luqum_replace_child supports BaseOperation, Group, and Unary; substitutes all equal direct children in order; preserves Luqum child container behavior; and raises the requested ValueError for unsupported parents.
TEST: pytest -q openlibrary/tests/solr/test_query_utils.py — 12 passed, 2 warnings.
No code defects or test environment problems found.
