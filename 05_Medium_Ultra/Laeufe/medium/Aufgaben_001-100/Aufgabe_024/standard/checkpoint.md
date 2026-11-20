Task: Fix catalog author matching for varied dates, honorifics, and literal asterisks.
Status: Complete. Updated staged author lookup to compare extracted birth/death years, added literal asterisk escaping, changed honorific removal to string input, and preserved incoming fields on new authors except temporary db_name metadata. Updated mock query behavior and regression tests.
Verification: pytest -q openlibrary/catalog/add_book/tests openlibrary/tests/catalog/test_utils.py (245 passed, 1 xfailed). git diff --check passed. Black unavailable in environment.
Constraints observed: No git history, index baseline, or harness configuration changes.
