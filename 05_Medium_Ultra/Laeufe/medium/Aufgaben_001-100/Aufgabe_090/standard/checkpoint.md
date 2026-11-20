Task: Fix /lists/add POST parameter precedence and flattened reconstruction.
Status: Complete.
Changes: Parse nonempty form bodies independently with parse_qs, apply defaults only to unrelated absent keys, skip invalid/empty seeds, and make unflatten honor later assignments. Added focused regression tests.
Verification: 17 focused tests passed; ruff and git diff --check passed. test_listapi.py could not collect because the existing cookielib dependency is unavailable.
