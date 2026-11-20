# Checkpoint

Issue: expose Project Runeberg identifiers consistently in work-search documents and add the requested Project Runeberg acquisition provider and public templates.

Progress: located work identifier aggregation in `openlibrary/solr/updater/work.py`, search-result shaping/default fields in `openlibrary/plugins/worksearch/`, and the acquisition interface in `openlibrary/book_providers.py`. The generic builder drops empty values, so Runeberg must be defaulted explicitly while leaving the other identifiers' existing aggregation unchanged. No repository-specific AGENTS.md files were found.

Implemented: added `ProjectRunebergProvider`, registered it with provider selection, and added its read/download templates. Work aggregation now always emits `id_project_runeberg` while preserving collected edition values and all other identifiers; work-search fetch defaults and shaped results expose an empty list when Solr has no value. Updated the existing exact-shape work-search fixture.

Verification: `pytest openlibrary/tests/solr/updater/test_work.py openlibrary/plugins/worksearch/tests/test_worksearch.py` passed (50 tests), and `pytest openlibrary/plugins/worksearch/tests` passed (4 tests). Only existing dependency deprecation warnings were reported. `git diff --check` passed.

Status: implementation and verification complete.
