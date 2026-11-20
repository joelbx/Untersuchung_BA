Updated [DocCLI.tty_ify](/app/lib/ansible/cli/doc.py) to render `L()`, `R()`, and `HORIZONTALLINE`, preserve the existing macro formats, and leave words such as `IBM(International Business Machines)` unchanged. Added focused tests in [test_doc.py](/app/test/units/cli/test_doc.py).

Validation: 30 CLI unit tests passed; `git diff --check` passed.