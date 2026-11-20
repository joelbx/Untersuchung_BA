# Checkpoint

Task: expose Project Runeberg identifiers in work search output and add provider integration.

Completed:
- Added `id_project_runeberg` as a list in every indexed work document, including `[]` when absent.
- Included the field in work search fetch/mapping and carousel queries.
- Added and registered `ProjectRunebergProvider` with catalog acquisition URL and OCAID recognition.
- Added Runeberg read and download templates.
- Added focused tests for populated/empty search documents, response mapping, and provider behavior.

Validation: 53 focused pytest tests pass; both templates compiled and rendered with and without analytics; Ruff and `git diff --check` pass. External Runeberg format URL availability was not checked because external research is blocked.
