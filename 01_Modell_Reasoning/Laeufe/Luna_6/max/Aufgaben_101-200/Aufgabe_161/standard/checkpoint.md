# Worksearch Solr JSON refactor checkpoint

- Objective: replace legacy XML response handling in Worksearch Solr requests with JSON and process flat facet count pairs.
- Replaced XML facet parsing with `process_facet` and `process_facet_counts` for Solr's flat JSON facet arrays.
- `run_solr_query` now always sends `wt`, defaulting to `json`; the Worksearch page parses JSON result documents, facets, and spellcheck suggestions.
- Converted `get_doc` to consume Solr JSON documents and updated the existing facet and document fixtures accordingly.
- Removed the Worksearch XML parser imports.
- Verification: `python -m pytest openlibrary/plugins/worksearch/tests/test_worksearch.py -q` passed (25 tests); `git diff --check` passed.
