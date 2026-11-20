# Checkpoint

Task: implement `luqum_replace_child` in `openlibrary/solr/query_utils.py`.

Completed: added a helper that accepts an `Item` parent and old/new child `Item`s, checks supported parent classes (`BaseOperation`, `Group`, `Unary`), and rebuilds `parent.children` as a tuple with all equal old children replaced. Unsupported parents raise the established `ValueError`.

Verification: `pytest -q openlibrary/tests/solr/test_query_utils.py` passed (6 tests); `git diff --check` passed.
