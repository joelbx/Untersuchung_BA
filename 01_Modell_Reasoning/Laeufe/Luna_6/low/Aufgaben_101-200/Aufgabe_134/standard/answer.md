Implemented Project Runeberg support:

- Work search documents now always include `id_project_runeberg` as an array, defaulting to `[]`.
- Added and registered `ProjectRunebergProvider`.
- Added Runeberg read button and download options templates.
- Added regression coverage for empty and populated identifier arrays.

Verification passed: 57 tests across work search updater and import tests. `git diff --check` passed.