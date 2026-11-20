Task: Add `luqum_replace_child` to `openlibrary/solr/query_utils.py`.

Status: Implemented `luqum_replace_child` and added coverage for supported parents, sequence types, equal matches, missing children, and unsupported parents. `python -m pytest openlibrary/tests/solr -q` passed (79 tests). `git diff --check` passed.
