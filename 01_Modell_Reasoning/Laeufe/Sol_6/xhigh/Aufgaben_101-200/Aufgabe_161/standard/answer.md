Updated Worksearch to request JSON by default and parse JSON search results, facets, spellcheck suggestions, and document fields. The new facet helpers preserve the required `has_fulltext` order and display values.

The Worksearch test suite passes: **28 tests**. `git diff --check` also passes.