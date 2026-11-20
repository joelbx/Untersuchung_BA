Task: Refactor Worksearch Solr response handling to JSON, update facet interfaces, and run relevant existing tests.
Status: Completed. Converted facet, spellcheck, and work document parsing to Solr JSON; defaulted run_solr_query wt to json. Updated Worksearch tests to use JSON and cover facet ordering, document fields, and wt selection.
Verification: pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py (27 passed); git diff --check (passed).
Constraints observed: Edited checked-out files only; did not alter git history, index baseline, or harness configuration.
