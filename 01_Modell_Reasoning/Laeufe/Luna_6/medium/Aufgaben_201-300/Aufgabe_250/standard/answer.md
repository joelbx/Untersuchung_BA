Added `luqum_replace_child` to [query_utils.py](/app/openlibrary/solr/query_utils.py). It supports `BaseOperation`, `Group`, and `Unary` parents, preserves child order and tuple type, and raises the specified `ValueError` for unsupported parents.

The existing query utility tests passed: **6 passed**.