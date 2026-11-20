Updated [DocCLI.tty_ify](/app/lib/ansible/cli/doc.py:77) to render links, references, and horizontal rules while preserving ordinary text such as `IBM(International Business Machines)`. Existing macro formats remain supported. Added [unit tests](/app/test/units/cli/test_doc.py).

Verification: 33 focused tests passed; `git diff --check` passed.