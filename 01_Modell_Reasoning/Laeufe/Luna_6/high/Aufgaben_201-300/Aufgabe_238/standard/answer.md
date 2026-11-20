Renamed the registered command to `:tab-select` and the completion providers to `tabs` and `other_tabs`. Existing index matching, count precedence, and cross-window focusing behavior are preserved. Updated the default `gt` binding, regenerated help, and renamed related test references.

Verification: the completion unit suites passed (154 passed, 1 xfailed); the focused tab completion tests passed (5 passed). The end-to-end run could not start the browser because QtWebKit is unavailable in this environment. `git diff --check` passed.

The required checkpoint is recorded in `.codex-role-output/checkpoint.md`.