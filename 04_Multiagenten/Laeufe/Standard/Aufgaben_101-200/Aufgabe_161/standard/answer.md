Worksearch now requests Solr JSON by default and reads search results, facets, and spellcheck suggestions from JSON. The new facet functions handle value/count pairs, including author names and ordered `has_fulltext` values. I updated the existing tests for JSON documents and responses.

Verification: all 27 Worksearch tests pass, and `git diff --check` is clean.