Updated Worksearch to read Solr JSON for facets, spellcheck suggestions, and work documents. `run_solr_query` now defaults `wt` to `json`, and the new facet functions handle value/count pairs and order the `has_fulltext` values as yes, then no.

The Worksearch tests pass: **27 passed**. `git diff --check` also passed.