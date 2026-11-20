VERDICT: ACCEPT

The patch adds `luqum_replace_child` in [query_utils.py](/app/openlibrary/solr/query_utils.py:35). Review found no correctness defect: it replaces equal direct children in order and raises the requested `ValueError` for unsupported parents.

`pytest -q openlibrary/tests/solr/test_query_utils.py` — **12 passed**, 2 warnings. No test environment problem was found.