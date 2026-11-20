Worksearch page searches now request JSON by default and read Solr documents, facets, and spellcheck suggestions from JSON. The new facet functions process flat value/count lists, including ordered `has_fulltext` yes/no entries. I also updated the template’s error rendering and replaced the XML test fixtures.

Verification: all 27 worksearch tests passed, and `git diff --check` was clean.