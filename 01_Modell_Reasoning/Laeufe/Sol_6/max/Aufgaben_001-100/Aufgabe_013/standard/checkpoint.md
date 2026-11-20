# Checkpoint

- Task: fix `ansible-doc` terminal rendering of documentation macros through `DocCLI.tty_ify`.
- Initial state: clean working tree; `DocCLI` calls `tty_ify` but does not define it locally.
- Implemented `DocCLI.tty_ify` for the requested macros with word boundaries and preserved horizontal rules through CLI paragraph wrapping.
- Added focused regression tests for macro rendering, ordinary words, and wrapped man text.
- Verification: `test/units/cli/test_cli.py` and `test/units/cli/test_doc.py` passed (40 tests); `git diff --check` passed; a temporary module passed end-to-end `ansible-doc` checks for links, references, horizontal rules, and ordinary words.
