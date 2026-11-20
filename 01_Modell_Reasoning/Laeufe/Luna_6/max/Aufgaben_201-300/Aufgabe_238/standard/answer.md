Implemented `:tab-select` as the registered command, with `tabs` and `other_tabs` completion providers. The command retains numeric and URL/title matching, `win_id/index` selection, count precedence, and window activation.

Updated the generated help, default `gt` binding, examples, and existing scenarios. The active help and source no longer reference `:buffer`.

- [commands.py](/app/qutebrowser/browser/commands.py:921)
- [miscmodels.py](/app/qutebrowser/completion/models/miscmodels.py:165)
- [commands help](/app/doc/help/commands.asciidoc:1433)

**Verification:** 73 completion unit tests passed; `git diff --check` passed. The end-to-end scenarios could not run: the harness forces QtWebKit, which is unavailable in this environment (11 startup failures, 1 skipped).