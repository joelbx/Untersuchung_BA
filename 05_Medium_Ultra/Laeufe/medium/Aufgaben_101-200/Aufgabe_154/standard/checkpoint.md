# Checkpoint

Task: repair Windows stderr CLIXML replacement.
Status: implemented and verified.
Changes: byte-accurate UTF-16-BE escape regex; valid CLIXML block replacement with UTF-8/cp437 decoding; Windows SSH exec integration; focused tests.
Verification: python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py (46 passed); git diff --check passed.
