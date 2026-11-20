Task: Centralize author base identifier generation for edition matching.
Status: Complete. add_db_name lives in catalog utils and runs during expand_record; existing edition conversion carries name and birth/death fields for expansion. Comparison handles inverted comma names so low-threshold matching still works with generated identifiers.
Verification: 71 passed, 1 xfailed, 2 xpassed in relevant catalog tests; ruff check and git diff --check passed.
Constraints observed: Local code/tests only; git history, index, and harness configuration untouched.
