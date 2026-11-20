Implemented Project Runeberg support.

- Work search documents now always include `id_project_runeberg` as an array, defaulting to `[]`.
- Added and registered `ProjectRunebergProvider`.
- Added Runeberg read button and download options templates.

Verification: the work-search suite passed (2 tests), and `git diff --check` passed. The attempted provider test path was not present in the repository.