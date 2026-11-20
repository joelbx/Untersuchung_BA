# Checkpoint

Task: Fix ansible-doc tty_ify macro rendering.
Status: Complete. Added DocCLI.tty_ify for I, B, M, U, C, L, R, and HORIZONTALLINE with protection for ordinary words such as IBM(...). Added focused unit coverage.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py (36 passed); git diff --check passed.
