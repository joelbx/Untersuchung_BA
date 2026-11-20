# Checkpoint

Task: Decode embedded Windows CLIXML stderr while preserving surrounding and invalid bytes.

Completed:
- Updated the PowerShell escaped UTF-16-BE code unit regex to require four explicit zero-prefixed hex bytes.
- Added `_replace_stderr_clixml` in the SSH plugin to replace complete embedded CLIXML blocks, use UTF-8 with cp437 fallback, and preserve unrelated or malformed stderr bytes.
- Changed Windows `exec_command` to call the helper.
- Added unit coverage for inline, multiline, repeated, adjacent, malformed, incomplete, cp437, and Unicode escape cases, plus the Windows execution path.

Checks:
- `python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py`: 50 passed.
- `git diff --check`: passed.
- `rg` is unavailable (`/bin/bash: line 1: rg: command not found`); used `grep` and `find` for repository inspection.
