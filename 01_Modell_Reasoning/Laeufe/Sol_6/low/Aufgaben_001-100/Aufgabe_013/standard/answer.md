Updated [DocCLI.tty_ify](/app/lib/ansible/cli/doc.py) to render `L()`, `R()`, and `HORIZONTALLINE`, preserve ordinary parenthesized words, and format multiple macros on one line. Existing macro output patterns remain covered.

Added focused tests in [test_doc.py](/app/test/units/cli/test_doc.py). The new tests and existing CLI tests pass: **35 passed**.