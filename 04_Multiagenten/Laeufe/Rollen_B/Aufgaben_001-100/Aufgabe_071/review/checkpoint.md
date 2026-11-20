VERDICT: ACCEPT
Reviewed lib/ansible/plugins/shell/powershell.py and test/units/plugins/shell/test_powershell.py against the issue requirements. No correctness or regression defect found. Matching stream text is concatenated within each Objs block, escapes and surrogate pairs are decoded, empty matches yield empty bytes, and unpaired surrogates use surrogatepass.
Tests executed:
- python -m pytest -q test/units/plugins/shell/test_powershell.py — 10 passed.
- python -m pytest -q test/units/plugins/shell — 15 passed.
TEST_ENVIRONMENT_PROBLEM: none.
No project code or tests changed during review.
