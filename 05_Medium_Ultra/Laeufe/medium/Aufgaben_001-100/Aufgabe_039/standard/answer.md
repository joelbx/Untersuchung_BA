Fixed `Booknotes.update_work_id` so a work ID collision rolls back the update and preserves every booknote. It now returns a dictionary with `rows_changed`, `rows_deleted`, and `failed_deletes`; a conflict returns `0`, `0`, and `1`. The admin caller now passes through that dictionary.

The relevant tests pass: **5 passed**, including the new conflict regression test.