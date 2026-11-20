Task: Fix Booknotes.update_work_id conflict handling.
Status: Complete. Booknotes now keeps its table intact when the target work already has notes, returns the required count dictionary, and updates the admin caller to retain that dictionary.
Verification: python -m pytest openlibrary/tests/core/test_db.py -q (6 passed); git diff --check (passed).
Delegation: None.
