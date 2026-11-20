Updated `GuiProcess` to stream both channels live, report stderr at error severity, and publish nonempty final summaries in stdout-then-stderr order. Extended the focused tests for live stderr, severity, ordering, and empty streams.

- [guiprocess.py](/app/qutebrowser/misc/guiprocess.py:191)
- [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py:152)

Verification: 45 focused tests passed; `git diff --check` passed.