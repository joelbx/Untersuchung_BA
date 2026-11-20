Added `luqum_replace_child` to [query_utils.py](/app/openlibrary/solr/query_utils.py:11). It replaces matching children in a tuple, preserves their order, and raises the existing `ValueError` for unsupported parent types.

The existing query utility tests passed: **6 passed**. `git diff --check` also passed.