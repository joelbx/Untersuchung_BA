# Checkpoint

Task: Decode embedded Windows stderr CLIXML while preserving surrounding and invalid data.
Status: Complete.
Changes: Tightened UTF-16-BE escape matching; added CLIXML replacement with UTF-8/cp437 decoding and invalid-block preservation; wired Windows SSH stderr through it; added parser and connection tests.
Verification: `PYTHONPATH=lib python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py` — 49 passed.
