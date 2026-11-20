Task: Remove legacy XML parsing from Worksearch Solr responses.
State: complete. Worksearch searches request JSON by default, decode JSON responses and facet fields, and build template documents from JSON dictionaries. Added process_facet and process_facet_counts, including boolean ordering, author facets, and language names. Added first_edition to requested fields.
Verification: pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py (27 passed); git diff --check (passed).
Delegation: none.
