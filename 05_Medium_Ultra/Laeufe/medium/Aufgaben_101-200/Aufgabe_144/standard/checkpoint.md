Task: relocate edition record expansion into catalog utils and update matching callers.
Status: complete. Added expand_record and relocated build_titles to catalog utils; updated add_book callers and tests; removed the old expansion function from merge_marc.
Verification: catalog merge and add_book tests: 85 passed, 8 skipped, 2 expected failures. Ruff and git diff --check passed.
