Task: Move build_marc record expansion to catalog.utils as expand_record and update all references, documentation, and tests.
Status: Complete. Moved title expansion dependency alongside expand_record, updated add_book callers and merge tests, and removed build_marc from merge_marc.
Verification: python -m pytest openlibrary/catalog/merge/tests openlibrary/catalog/add_book/tests -q (84 passed, 8 skipped, 2 xfailed). git diff --check passed; ruff check of modified Python files passed.
Constraints observed: Used local repository code and existing tests only; did not change git history, index baseline, or harness configuration.
