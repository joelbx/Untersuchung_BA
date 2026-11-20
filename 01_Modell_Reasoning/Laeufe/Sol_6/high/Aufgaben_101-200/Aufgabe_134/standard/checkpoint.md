# Checkpoint

Task: expose `id_project_runeberg` as an array in every work search document and add the Project Runeberg acquisition provider and templates.

Status: implemented the work search field in the Solr builder, default search field selection, page response mapping, and `/search.json` response normalization. Added and registered `ProjectRunebergProvider`, both Runeberg templates, and focused tests. Repository was initially clean. External research was unavailable; only local code and tests were used.

Verification: 56 focused tests passed, including work search, work and edition indexers, provider selection, and template rendering. Ruff checks and `git diff --check` passed. No git history or index baseline was changed.
