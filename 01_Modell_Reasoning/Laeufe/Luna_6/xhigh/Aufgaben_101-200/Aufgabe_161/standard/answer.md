Implemented the Worksearch Solr JSON refactor. `run_solr_query` now defaults `wt` to `json`; search results and documents are parsed as JSON; and the new facet processors handle boolean ordering, author facets, and language display names.

Updated the Worksearch tests to use JSON fixtures. Verification: **26 tests passed**, and `git diff --check` passed.

Changed: [code.py](/app/openlibrary/plugins/worksearch/code.py), [test_worksearch.py](/app/openlibrary/plugins/worksearch/tests/test_worksearch.py).