Added `luqum_replace_child` in [query_utils.py](/app/openlibrary/solr/query_utils.py:11). It replaces all equal direct children while preserving their order and sequence type, leaves children unchanged when there is no match, and raises the specified `ValueError` for unsupported parents.

Verification: all 6 existing query utility tests passed, along with direct checks of the new behavior.