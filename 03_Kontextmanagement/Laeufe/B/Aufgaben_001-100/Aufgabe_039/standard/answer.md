Fixed `Booknotes.update_work_id` so a target `work_id` conflict preserves every booknote and returns `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}`. The admin caller now retains the result as a dictionary.

The relevant core database tests pass: **6 passed**.