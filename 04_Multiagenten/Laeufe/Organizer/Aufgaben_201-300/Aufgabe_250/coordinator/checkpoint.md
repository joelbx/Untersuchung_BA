Task: Add luqum_replace_child(parent, old_child, new_child) in openlibrary/solr/query_utils.py.
Status: Implemented supported-parent validation and equality-based replacement preserving child sequence type. Added tests for BaseOperation, Group, Unary, repeated equal children, absent child, unsupported SearchField.
Verification: pytest -q openlibrary/tests/solr/test_query_utils.py: 12 passed.
Constraints observed: no external research, no git history/index/harness changes.
