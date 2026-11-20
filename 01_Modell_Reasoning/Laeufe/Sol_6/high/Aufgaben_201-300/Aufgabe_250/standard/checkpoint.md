Task: Add `luqum_replace_child` in `openlibrary/solr/query_utils.py` and verify with existing relevant tests.

Status: Completed. Added the helper with supported parent validation, equality-based replacement of all direct matches, preservation of child order and sequence type, and no assignment when no match exists.

Verification: `pytest -q openlibrary/tests/solr/test_query_utils.py` passed (6 tests). Direct local checks passed for BaseOperation, Group, Unary, duplicate equal children, absent child, and unsupported Item. `git diff --check` passed.
