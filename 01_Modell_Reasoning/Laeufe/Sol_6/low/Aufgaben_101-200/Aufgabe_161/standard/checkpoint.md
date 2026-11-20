# Checkpoint

Resolved Worksearch XML parsing path in checked-out files. `run_solr_query` now supplies `wt=json` by default; `do_search`, facet processing, and `get_doc` consume Solr JSON. Updated existing Worksearch tests for JSON facet and document shapes. Verification: `python -m pytest openlibrary/plugins/worksearch/tests/test_worksearch.py -q` (25 passed).
