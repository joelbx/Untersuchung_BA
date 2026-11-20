Updated [DocCLI.tty_ify](/app/lib/ansible/cli/doc.py) to render `L()`, `R()`, and `HORIZONTALLINE`, preserve the existing macro formats, and leave ordinary text such as `IBM(International Business Machines)` unchanged. Added [unit tests](/app/test/units/cli/test_doc.py) for mixed macros and unsupported text.

Validation: 31 CLI unit tests passed, and a local `ansible-doc` invocation succeeded.