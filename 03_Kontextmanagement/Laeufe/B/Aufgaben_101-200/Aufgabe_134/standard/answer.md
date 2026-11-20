Resolved the Runeberg issue in `/app`. Work search documents now include `id_project_runeberg` as an array, including `[]` when absent, while other identifier fields retain their values. I added `ProjectRunebergProvider` and the Runeberg read and download templates.

Verification passed: 53 relevant Solr tests, provider and template rendering checks, and Ruff.