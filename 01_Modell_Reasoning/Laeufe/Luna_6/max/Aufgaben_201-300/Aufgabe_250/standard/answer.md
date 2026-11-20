Implemented `luqum_replace_child` in [query_utils.py](/app/openlibrary/solr/query_utils.py:35). It replaces equal direct children while preserving their order and sequence type, leaves children unchanged if there’s no match, and raises the existing `ValueError` for unsupported parents.

Verification: `pytest -q openlibrary/tests/solr/test_query_utils.py` passed (6 tests).