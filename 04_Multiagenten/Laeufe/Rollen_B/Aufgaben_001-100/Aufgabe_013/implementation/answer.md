Implemented `DocCLI.tty_ify` to render `L()`, `R()`, and `HORIZONTALLINE`, preserve ordinary parenthesized words, and format multiple macros in one line. Existing `I()`, `B()`, `M()`, `U()`, and `C()` output is retained.

Added focused tests in [test_doc.py](/app/test/units/cli/test_doc.py). All 31 relevant CLI unit tests pass, and `git diff --check` is clean.