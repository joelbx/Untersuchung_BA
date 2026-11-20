# Checkpoint

- Task: decode embedded CLIXML in Windows SSH stderr while preserving unrelated and malformed bytes.
- Located implementation in `lib/ansible/plugins/connection/ssh.py` and CLIXML parser in `lib/ansible/plugins/shell/powershell.py`.
- Implemented `_replace_stderr_clixml` in SSH connection handling and corrected the UTF-16-BE escape pattern in the PowerShell parser.
- Added unit coverage for embedded, multiline, malformed, incomplete, repeated, UTF-8, and cp437 CLIXML plus the Windows `exec_command` path.
- Verified with `PYTHONPATH=lib pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py` (49 passed).
