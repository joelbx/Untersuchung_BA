# Worksearch Solr JSON migration

Status: complete. Worksearch requests JSON by default and processes JSON facets, spellcheck suggestions, and work documents. The search error template displays string errors. Updated the existing Worksearch tests for JSON and added coverage for facet order, field mapping, query format, and errors. Verification: 31 focused tests passed; git diff --check passed.
