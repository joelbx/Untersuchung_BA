# Checkpoint

Implemented Project Runeberg work-search exposure and provider integration.

- Work Solr builder always sets `id_project_runeberg` to an array, including `[]` when absent.
- Work search fetches and returns the field with an empty-array fallback.
- Registered `ProjectRunebergProvider` with OCAID matching and open-access acquisition links.
- Added Runeberg read-button and download-option templates.
- Updated tests for populated and absent Runeberg identifiers.

Verification: 51 relevant pytest tests passed; `git diff --check` passed; provider behavior and both templates compiled in a local smoke check.
