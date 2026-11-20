# Checkpoint

Task: Repair Windows stderr CLIXML replacement in the checked-out repository.

Implemented:
- Replaced complete embedded CLIXML blocks in SSH Windows stderr while retaining surrounding and malformed bytes.
- Added UTF-8 decoding with cp437 fallback for CLIXML content.
- Tightened UTF-16-BE escape matching and accepted valid `<Objs>` elements without attributes.
- Added focused SSH replacement, integration-path, and Unicode escape tests.

Verification:
- `python -m pytest -q test/units/plugins/connection/test_ssh.py test/units/plugins/shell/test_powershell.py`: 44 passed, exit 0.
- `git diff --check`: exit 0.

Environment note: `rg` is unavailable (`/bin/bash: line 1: rg: command not found`); local grep/find were used. No downloads or external research.
