Updated Worksearch to consume Solr JSON for search results, facets, spellcheck suggestions, and documents. `run_solr_query` now defaults `wt` to `json`, and facet processing uses the new tuple based interfaces.

The updated Worksearch tests pass: **25 passed**.