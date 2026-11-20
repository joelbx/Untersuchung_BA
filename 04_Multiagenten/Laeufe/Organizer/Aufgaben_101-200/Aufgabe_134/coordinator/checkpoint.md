# Checkpoint

Task: expose `id_project_runeberg` as an array in every work search document, and add Project Runeberg acquisition provider and public templates.

Completed: registered `ProjectRunebergProvider`; added Runeberg read and download templates; included identifier in work Solr builder, default search fields, search document adapter, JSON search responses, and carousel query fields. Added focused tests for provider, work indexing, and search shapes.

Verification: 56 focused pytest cases passed; both templates rendered with and without the optional analytics callback; Ruff lint and `git diff --check` passed. Black is unavailable locally. No delegation was used.
