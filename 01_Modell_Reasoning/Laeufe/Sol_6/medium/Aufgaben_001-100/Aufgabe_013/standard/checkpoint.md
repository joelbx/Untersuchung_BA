# Checkpoint

Implemented `DocCLI.tty_ify` for documentation macros, including L(), R(), and HORIZONTALLINE, while preserving ordinary words containing parentheses. Added focused unit coverage for links, references, mixed macros, horizontal rules, and unsupported text.

Validation: `PYTHONPATH=lib:test pytest -q test/units/cli/test_doc.py test/units/cli/test_cli.py` (31 passed); `PYTHONPATH=lib bin/ansible-doc -M test/integration/targets/ansible-doc/library test_docs` succeeded; `git diff --check` passed.
