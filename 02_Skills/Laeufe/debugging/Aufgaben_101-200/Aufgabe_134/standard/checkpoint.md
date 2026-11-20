# Checkpoint

Task: expose `id_project_runeberg` in work search documents with an array shape; add Project Runeberg acquisition provider and templates.

Status: investigating repository paths and existing behavior. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep`.

Constraints: no external research or downloads; preserve git history and index baseline.

Investigation: edition configuration defines `project_runeberg`; EditionSolrBuilder maps edition identifiers to `id_*` arrays, and WorkSolrBuilder aggregates them. Solr schema has multivalued `id_*`. Work search default fetched fields and `get_doc` explicitly list provider IDs but omit Runeberg. Hypothesis: omitted retrieval/mapping causes the reported missing field. A regression test for missing and populated Runeberg IDs failed before implementation with absent `id_project_runeberg` (command: `python -m pytest openlibrary/plugins/worksearch/tests/test_worksearch.py -q`, exit 1).

Implemented: work-search default fetch and response mapping now include `id_project_runeberg` with `[]` fallback; provider is registered and exposes open-access edition URL; download/read templates added; carousel explicitly fetches the field. Existing generic Solr identifier indexing was retained. Added tests for work aggregation, empty/populated response shapes, provider behavior, and template rendering.

Verification: `python -m pytest openlibrary/plugins/worksearch/tests/test_worksearch.py openlibrary/tests/solr/updater/test_work.py openlibrary/tests/test_book_providers_runeberg.py -q` passed (54 tests). `python -m ruff check ...` passed; `git diff --check` passed. Template rendering was also exercised directly. External Runeberg download endpoint availability could not be confirmed from local evidence; external research is blocked.
