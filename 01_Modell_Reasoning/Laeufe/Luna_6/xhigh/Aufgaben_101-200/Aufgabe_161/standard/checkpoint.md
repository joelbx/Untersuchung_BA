# Worksearch Solr JSON refactor checkpoint

Task: remove XML parsing from the Worksearch Solr search path, implement JSON-based document and facet handling, ensure `run_solr_query` always sends `wt` (default `json`), and run relevant existing tests.

Completed:
- Added `process_facet` and `process_facet_counts` for flat JSON facet values, author key/name extraction, language display translation, and ordered `has_fulltext` values.
- Added `wt=json` by default in `run_solr_query` while preserving an explicitly supplied value.
- Migrated Worksearch search response and document handling to JSON; included `first_edition` in the default requested fields.
- Replaced XML-only tests with JSON facet and document coverage.
- Confirmed no XML parsing references remain in `code.py` or the updated test module.

Verification: `pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py` — 26 passed. `git diff --check` passed.
