Updated Worksearch to request JSON from Solr by default and read JSON facets, spellcheck suggestions, and documents. Added `process_facet` and `process_facet_counts`, including boolean facet ordering, author names, and language names. Updated the search template to display parsing errors.

Verification: all 28 Worksearch tests pass, and `git diff --check` passes.