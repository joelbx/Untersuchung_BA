Updated Worksearch to request Solr JSON by default and parse JSON search results, documents, spellcheck, and facets. Added the requested facet functions and replaced the XML based tests with JSON coverage.

Verification: 29 Worksearch tests passed; `git diff --check` and Python compilation passed.