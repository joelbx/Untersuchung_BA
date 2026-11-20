Updated [DocCLI.tty_ify](/app/lib/ansible/cli/doc.py) to render `L()`, `R()`, and `HORIZONTALLINE`, preserve ordinary text such as `IBM(International Business Machines)`, and keep the existing macro formats. Added [focused tests](/app/test/units/cli/test_doc.py) for mixed macros and spacing.

Verification: 30 relevant CLI unit tests passed; `git diff --check` passed.