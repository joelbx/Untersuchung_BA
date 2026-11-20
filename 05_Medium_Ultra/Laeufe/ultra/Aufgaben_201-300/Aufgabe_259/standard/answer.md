Fixed [Solr work document selection](/app/openlibrary/solr/update_work.py:746): a public IA edition now takes priority for `lending_edition_s`, and `lending_identifier_s` comes from that same edition. `lendinglibrary` editions are classified as loanable.

Updated [regression tests](/app/openlibrary/tests/solr/test_update_work.py:302) to cover mixed editions, multiple print-disabled IDs, collection and IA ID aggregation, and lending fallback. Two agents helped inspect the builder and add tests; I integrated and verified the patch.

`python -m pytest openlibrary/tests/solr -q`: **61 passed**. `git diff --check`: passed.