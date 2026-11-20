Worksearch now requests JSON by default and reads Solr results, facets, spellcheck suggestions, and documents from JSON. The new facet functions handle boolean ordering, author IDs and names, and language names.

The Worksearch tests pass: **27 passed**. `git diff --check` also passed. I completed the changes without delegation.