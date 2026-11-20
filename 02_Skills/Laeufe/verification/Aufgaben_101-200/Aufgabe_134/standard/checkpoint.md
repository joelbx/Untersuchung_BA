# Checkpoint

Task: expose `id_project_runeberg` as a list in every work search document and add a Project Runeberg provider and templates.

Changes: work Solr builder initializes `id_project_runeberg` to `[]`; work-search field selection and response mapping include it; provider registration supplies open-access edition links; read/download templates added. Regression tests cover populated and empty identifiers, preservation of another identifier, provider behavior, and template rendering.

Verification:
- `python -m pytest openlibrary/tests/solr/updater openlibrary/plugins/worksearch/tests openlibrary/tests/test_project_runeberg_provider.py -q` — 59 passed, 3 unrelated deprecation warnings, exit 0.
- `ruff check openlibrary/book_providers.py openlibrary/plugins/worksearch/code.py openlibrary/plugins/worksearch/schemes/works.py openlibrary/plugins/worksearch/tests/test_worksearch.py openlibrary/solr/updater/work.py openlibrary/tests/solr/updater/test_work.py openlibrary/tests/test_project_runeberg_provider.py` — all checks passed, exit 0.
- `git diff --check` — exit 0.
- `black --check openlibrary/book_providers.py openlibrary/plugins/worksearch/code.py openlibrary/plugins/worksearch/schemes/works.py openlibrary/plugins/worksearch/tests/test_worksearch.py openlibrary/solr/updater/work.py openlibrary/tests/solr/updater/test_work.py openlibrary/tests/test_project_runeberg_provider.py` — unavailable: `/bin/bash: line 1: black: command not found` (exit 127). Formatting with Black remains unchecked.
- `ruff format --check` on the same seven Python files — exit 1: it would reformat all seven files, including existing repository formatting. Did not apply unrelated formatting changes.

Uncertainty: local metadata documents Project Runeberg edition URLs (`https://runeberg.org/<id>/`) but no verified format-specific download endpoints. The download-options template links each listed format to the edition page for discovery; direct format URLs were not verified. External research is blocked.
