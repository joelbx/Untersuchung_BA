Updated Worksearch to request Solr JSON by default and read facets, spelling suggestions, and documents from JSON. The new facet processors handle flat value/count pairs, including ordered `has_fulltext` values.

The relevant Worksearch tests pass: **28 passed**. `git diff --check` also passed.