# Checkpoint

Task: Fix Windows stderr handling for embedded CLIXML in `/app`.

Completed:
- Corrected the UTF-16-BE escape matcher in the PowerShell parser.
- Added `_replace_stderr_clixml` in the SSH connection plugin. It scans line headers, parses complete embedded blocks, uses UTF-8 with cp437 fallback, preserves surrounding bytes, and leaves invalid or incomplete blocks unchanged.
- Updated Windows `exec_command` handling to use the helper.

Validation: `python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py` passed (35 tests). `git diff --check` passed.
