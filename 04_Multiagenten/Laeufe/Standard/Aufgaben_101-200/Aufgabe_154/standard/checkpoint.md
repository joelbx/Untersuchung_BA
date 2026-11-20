Task: Decode embedded CLIXML in Windows SSH stderr while preserving surrounding and invalid bytes.
Status: Implemented line-aware CLIXML replacement in ssh.py, UTF-8/cp437 handling, adjacent Objs handling, and stricter UTF-16-BE escape matching in powershell.py. Added regression coverage including Windows exec_command.
Validation: python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py (48 passed).
