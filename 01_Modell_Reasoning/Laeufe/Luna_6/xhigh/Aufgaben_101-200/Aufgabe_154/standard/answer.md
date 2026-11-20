Implemented Windows stderr CLIXML replacement in [ssh.py](/app/lib/ansible/plugins/connection/ssh.py), including UTF-8 decoding with cp437 fallback and preservation of surrounding bytes. Updated the UTF-16BE escape matcher in [powershell.py](/app/lib/ansible/plugins/shell/powershell.py).

The existing SSH and PowerShell unit tests passed: **35 passed**. `git diff --check` passed.