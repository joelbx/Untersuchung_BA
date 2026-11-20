Work-search documents now expose `id_project_runeberg` as an array, including `[]` when no Runeberg ID exists. Other identifier fields retain their values. I also registered `ProjectRunebergProvider` and added the read button and download-options templates.

Verification: 59 relevant tests passed, Ruff lint passed, and `git diff --check` passed. Black was unavailable; Ruff’s formatter check reported differences across the checked Python files.

The download options link to the Runeberg edition page for each format. The repository documents that page URL but provides no verified direct format URLs, so direct downloads remain unverified.