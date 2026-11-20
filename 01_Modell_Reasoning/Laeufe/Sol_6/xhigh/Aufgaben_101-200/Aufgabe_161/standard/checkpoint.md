# Worksearch Solr JSON migration

Completed: Worksearch HTML queries now request and parse Solr JSON. Facet processors consume JSON flat lists and return ordered display triples; document conversion reads JSON fields. XML fixtures were replaced with JSON coverage. `pytest -q openlibrary/plugins/worksearch/tests` passed (28 tests), and `git diff --check` passed.
