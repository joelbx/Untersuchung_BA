Task: Fix Windows SSH stderr CLIXML replacement.
Status: implementation complete and focused tests passing.
Changes: embedded block replacement with UTF-8/cp437 handling and malformed-block preservation; corrected UTF-16-BE escape regex; added focused and exec integration tests.
Verification: pytest -q test/units/plugins/connection/test_ssh.py test/units/plugins/shell/test_powershell.py (47 passed); git diff --check passed.
Delegation: none.
