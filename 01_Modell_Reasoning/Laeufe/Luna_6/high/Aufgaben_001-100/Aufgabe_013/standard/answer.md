Implemented `DocCLI.tty_ify(text)` to render the requested macros, preserve unsupported parenthesized text, and handle multiple macros on a line. Added focused unit tests in [test_doc.py](/app/test/units/cli/test_doc.py).

Verification: all 3 focused tests passed, and `git diff --check` passed. `ansible-test` could not run because its Python 3.8 environment lacks pytest.