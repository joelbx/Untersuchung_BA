Task: add `luqum_replace_child` to `openlibrary/solr/query_utils.py`.

Implemented `luqum_replace_child` with the same supported parent types and error message as `luqum_remove_child`. It rebuilds the children in order and replaces every matching child. Added tests for all supported types, absent children, repeated matches, and unsupported parents.

Verification: `pytest -q openlibrary/tests/solr/test_query_utils.py` passed (11 tests); `git diff --check` passed.
