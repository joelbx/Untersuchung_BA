Work search documents now include `id_project_runeberg` as an array, with `[]` when no identifier is present. The change preserves the existing identifier fields. I also registered `ProjectRunebergProvider` and added its Read button and download options templates.

The download options link to the Project Runeberg edition page, where readers can find the listed formats; they are not direct format downloads.

Verification: 56 relevant tests passed, both templates rendered, and Ruff lint and `git diff --check` passed. No delegation was used.