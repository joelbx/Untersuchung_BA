Implemented Windows stderr CLIXML handling.

- Added [`_replace_stderr_clixml` in `ssh.py`](/app/lib/ansible/plugins/connection/ssh.py:412) to replace complete embedded blocks, preserve surrounding bytes, use cp437 when UTF-8 decoding fails, and leave malformed or incomplete blocks unchanged. Windows `exec_command` now uses it.
- Updated [`_STRING_DESERIAL_FIND`](/app/lib/ansible/plugins/shell/powershell.py:32) to match UTF-16-BE hex bytes explicitly and preserve Unicode lookalikes.

Verification: 35 existing PowerShell and SSH unit tests passed; targeted smoke checks and `git diff --check` passed.