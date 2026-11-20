Task: resolve inconsistent edition matching and record expansion.
Status: complete. Implemented add_db_name, expand_record, threshold_match in merge_marc; utils reexports the first two. Edition matching and add_book call path accept raw records. Added regression tests for dates, ISBNs, missing title/ISBN, raw comparisons, and thresholds.
Verification: ruff check and git diff --check passed. Relevant pytest run: 75 passed, 2 existing xfailed.
Delegation: none.
