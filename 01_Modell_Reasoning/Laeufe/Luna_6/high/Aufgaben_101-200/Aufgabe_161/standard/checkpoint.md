# Checkpoint

Task: refactor Worksearch Solr requests and facet processing to use JSON output.

Completed:
- `run_solr_query` now defaults the Solr `wt` parameter to `json`.
- `do_search` parses Solr JSON response/docs, facet arrays, and spellcheck suggestions.
- Added `process_facet` and `process_facet_counts`; boolean facet rows put `true` before `false`.
- Converted `get_doc` to consume JSON documents and included `first_edition` in the default field list.
- Updated the existing Worksearch tests to use JSON shaped docs and facet data.

Verification: `python -m pytest openlibrary/plugins/worksearch/tests/test_worksearch.py -q` passed (25 tests); `git diff --check` passed.
