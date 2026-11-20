Task: Remove legacy XML parsing from Worksearch Solr output.
Status: Complete. Worksearch now requests JSON by default and parses JSON facets, spellcheck suggestions, and documents. XML parsing and its obsolete test fixture were removed.
Verification: pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py (29 passed).
