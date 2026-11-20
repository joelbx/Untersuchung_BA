# Worksearch Solr JSON migration checkpoint

- Replaced XML parsing in the Worksearch page query, facets, spellcheck, and document adapter with Solr JSON handling.
- `run_solr_query` includes `wt`, defaulting to `json`.
- Added `process_facet` and `process_facet_counts` for flat JSON facet arrays.
- Replaced XML tests with JSON tests and added query, spellcheck, facet, and invalid response coverage.
- `rg` was unavailable (`/bin/bash: rg: command not found`); used `grep` and `find`.
- Initial new query test failed because test configuration has no `solr_select_url`; the test now supplies a local URL.
- Verification: `pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py && git diff --check && python -m compileall -q openlibrary/plugins/worksearch/code.py` passed, 29 tests, exit 0, before removal of a commented XML test block. Final verification follows.
- Final verification after all code and test edits: `pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py && git diff --check && python -m compileall -q openlibrary/plugins/worksearch/code.py && git status --short` exited 0; 29 tests passed, with two dependency warnings.
