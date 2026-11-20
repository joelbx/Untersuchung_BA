Added `luqum_replace_child` to [query_utils.py](/app/openlibrary/solr/query_utils.py). It replaces every equal direct child in order, leaves unmatched children unchanged, and raises the existing `ValueError` for unsupported parents.

Added tests for the supported parent types and edge cases. All 12 tests in `test_query_utils.py` pass.