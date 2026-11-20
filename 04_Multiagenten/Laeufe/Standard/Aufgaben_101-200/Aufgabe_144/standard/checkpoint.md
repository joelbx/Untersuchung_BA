Task: relocate build_marc to catalog.utils.expand_record and update callers/tests.
Status: complete. Moved title expansion and edition expansion to catalog.utils; updated add_book and matching callers, documentation, and tests. Removed build_marc from merge_marc.
Verification: pytest -q openlibrary/catalog/merge/tests openlibrary/catalog/add_book/tests => 84 passed, 8 skipped, 2 xfailed. ruff check on modified Python files passed; git diff --check passed.
