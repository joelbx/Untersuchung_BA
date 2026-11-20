Worksearch now requests JSON by default and reads facets, spellcheck suggestions, and work documents from Solr’s JSON response. The new facet processors preserve the required `has_fulltext` order and display values. I also updated the search error display and the existing tests.

Verification: **31 Worksearch tests passed**; `git diff --check` passed.