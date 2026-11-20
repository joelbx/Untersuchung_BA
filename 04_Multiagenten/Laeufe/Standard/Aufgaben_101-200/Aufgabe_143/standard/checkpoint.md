Task: centralize author base identifier generation for edition matching.
Status: implemented add_db_name in catalog.utils, called during expand_record; existing-edition conversion now carries name and birth/death dates only. Updated focused tests and the nearby-date threshold fixture.
Verification: catalog add_book and merge tests: 105 passed, 1 skipped, 2 xfailed, 1 xpassed. git diff --check passed.
