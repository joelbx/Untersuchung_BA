# Checkpoint

Implemented embedded CLIXML replacement for Windows SSH stderr in `powershell.py` and switched `ssh.py` to use it for Windows shells. Updated the UTF-16-BE escape matcher.

Verification: `python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py` passed (35 tests). `git diff --check` passed.
