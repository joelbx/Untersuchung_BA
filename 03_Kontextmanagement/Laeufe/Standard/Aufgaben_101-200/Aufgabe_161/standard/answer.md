Worksearch now reads Solr JSON for facets, spellcheck suggestions, and work documents. The query defaults to `wt=json`, and the new facet functions handle flat value/count pairs, including ordered `has_fulltext` values.

The updated Worksearch tests pass: **28 passed**. `git diff --check` also passed.