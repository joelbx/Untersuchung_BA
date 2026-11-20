Task: Add module-level make_date_string and validate patron check-in updates.
Status: Complete. Added module-level date formatter, retained check_ins method compatibility, added patron_check_ins update handler with required-field and ownership checks, and made BookshelvesEvents.update_event_data callable as a class method.
Verification: python -m pytest openlibrary/plugins/upstream/tests/test_checkins.py openlibrary/tests/core/test_db.py -q (19 passed); git diff --check passed.
Note: test_db.py alone hits an existing circular import during collection; combined run passes.
Constraints observed: Used local code/tests only; did not change git history, index baseline, or harness configuration.
