Task: fix ansible-doc documentation macro rendering.
Found: DocCLI inherits CLI.tty_ify, which handles only I/B/M/U/C and can match inside words.
Plan: implement DocCLI.tty_ify for the requested output and run existing CLI tests.
Done: implemented the formatter, added focused scenarios, and ran test_doc.py plus test_cli.py (35 passed).
