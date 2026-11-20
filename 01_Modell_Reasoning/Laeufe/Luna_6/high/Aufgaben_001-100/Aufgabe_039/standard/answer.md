Updated [booknotes.py](/app/openlibrary/core/booknotes.py) so a conflicting `work_id` leaves booknotes intact and returns `rows_changed`, `rows_deleted`, and `failed_deletes`. The admin redirect summary now retains that dictionary result.

Validation: `python -m pytest openlibrary/tests/core/test_db.py -q` passed (2 tests); `git diff --check` passed.