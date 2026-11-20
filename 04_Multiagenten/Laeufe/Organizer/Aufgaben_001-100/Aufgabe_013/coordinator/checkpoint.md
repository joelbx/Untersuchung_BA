Task: Fix ansible-doc documentation macro rendering through DocCLI.tty_ify(text).
Status: Implemented DocCLI-specific macro rendering with word boundary protection. Added focused tests for links, references, horizontal rule, multiple macros, and ordinary parenthesized text.
Validation: PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py (30 passed). Full test/units/cli suite has unrelated order/state failures (9 failed, 59 errors); isolated Galaxy test passes both alone and after new tests. No delegation used.
