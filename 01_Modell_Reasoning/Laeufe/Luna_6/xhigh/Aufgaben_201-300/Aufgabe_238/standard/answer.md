Replaced the registered `:buffer` command with [`:tab-select` in commands.py](/app/qutebrowser/browser/commands.py:921), preserving numeric and title/URL matching, count precedence, cross-window selection, and window focus. Renamed the completion providers to [`tabs` and `other_tabs`](/app/qutebrowser/completion/models/miscmodels.py:165).

Updated the generated [command help](/app/doc/help/commands.asciidoc:128), the default `gt` binding, and existing tests and examples. No active `:buffer` command or old completion-provider references remain outside the historical changelog.

**Validation:** 73 completion unit tests passed; 13 focused end-to-end scenarios passed and 1 was skipped. `git diff --check` passed. The doc check reported the intentionally modified generated help files.