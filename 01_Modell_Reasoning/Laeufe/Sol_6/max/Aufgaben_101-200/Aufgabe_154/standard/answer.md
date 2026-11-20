Updated [ssh.py](/app/lib/ansible/plugins/connection/ssh.py) to decode embedded CLIXML in Windows stderr, with cp437 fallback, while preserving surrounding bytes and malformed blocks. Tightened the UTF-16-BE escape regex in [powershell.py](/app/lib/ansible/plugins/shell/powershell.py) and added regression tests.

Verification: 52 targeted tests passed; `git diff --check` passed.