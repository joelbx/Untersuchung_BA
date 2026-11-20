Updated [DocCLI.tty_ify](/app/lib/ansible/cli/doc.py:77) to render `L()`, `R()`, and `HORIZONTALLINE`, while preserving ordinary parenthesized words and the existing macro formats. Added regression coverage for mixed macros.

Verification: 36 relevant unit tests passed; `git diff --check` passed.