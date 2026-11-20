Replaced the registered `:buffer` command with `:tab-select`, renamed its tab completion providers, and updated the default `gt` binding, help pages, examples, and affected tests. Tab selection retains index, title and URL matching, count precedence, and cross-window focus behavior.

Verification: 154 completion unit tests passed with one expected failure; nine focused completion tests passed; 12 tab selection end to end scenarios passed with one skipped; four completion end to end scenarios passed. `git diff --check` is clean.

No delegation was used.