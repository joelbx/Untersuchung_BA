Fixed `Booknotes.update_work_id` so a work ID conflict rolls back the update and preserves every booknote. It now returns a dictionary with `rows_changed`, `rows_deleted`, and `failed_deletes`; a conflict reports `0`, `0`, and `1`. I updated the admin caller and added regression tests.

Verification: `python -m pytest openlibrary/tests/core/test_db.py -q` — 5 passed.