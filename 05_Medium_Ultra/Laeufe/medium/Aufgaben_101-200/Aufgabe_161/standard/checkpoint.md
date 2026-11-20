Task: Remove legacy XML parsing from Worksearch Solr output.
Status: Complete. Worksearch search responses, facets, spellcheck, and work documents now use Solr JSON. run_solr_query defaults wt to json while respecting an explicit value.
Verification: pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py (28 passed); git diff --check (passed).
Files changed: openlibrary/plugins/worksearch/code.py; openlibrary/plugins/worksearch/tests/test_worksearch.py.
