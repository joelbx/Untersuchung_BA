# Checkpoint

Task: expose `id_project_runeberg` as an array in every work search document, and add the Project Runeberg acquisition provider and public templates.

Initial state: working in `/app`; local repository inspection is underway. External research is unavailable. `rg` is not installed, so repository searches use `find` and `grep`.

Findings: `EditionSolrBuilder.identifiers` already maps edition `project_runeberg` values to `id_project_runeberg`; `WorkSolrBuilder.build_identifiers` aggregates them but does not emit an empty field. `WorkSearchScheme.default_fetched_fields` and `get_doc` omit the field. The provider interface and registration are in `openlibrary/book_providers.py`; templates are in `openlibrary/templates/book_providers/`.

Implemented: work builder emits `id_project_runeberg` as an array even when absent; work search fetches and exposes it; the Project Runeberg provider is registered; read and download templates are added. Focused tests cover populated and empty identifiers, other identifier fields, and provider selection/acquisitions.

Verification complete: 53 relevant pytest tests passed after the final shape normalization change; Ruff and `git diff --check` passed. Both templates compiled and rendered in a local smoke check, including the optional analytics callback and once-only toast. Download URLs could not be live checked because external research is blocked.
