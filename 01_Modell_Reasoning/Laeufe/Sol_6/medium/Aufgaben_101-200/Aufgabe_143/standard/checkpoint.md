Task: centralize author base identifiers during edition expansion.
Status: complete. add_db_name moved to catalog utils; expand_record invokes it; existing editions provide only name and birth/death dates before expansion; comparator handles inverted names.
Verification: 72 passed, 1 xfailed, 2 xpassed in relevant catalog tests; git diff --check passed. Ruff reports pre-existing duplicate normalize_import_record import in test_add_book.py.
