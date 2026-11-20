Updated work-search results to include `id_project_runeberg` as an array for every work, using `[]` when no Runeberg identifier is present. Added `ProjectRunebergProvider` and the requested read-button and download-options templates.

The work-search tests pass (3 tests), including a case with Runeberg identifiers alongside an existing identifier. `git diff --check` also passes.