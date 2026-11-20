Task: Move catalog edition expansion from build_marc to catalog.utils.expand_record; update callers, docs, and tests.
Status: Complete. Moved build_titles and expansion into catalog.utils, removed build_marc from merge_marc, updated add_book callers and tests. No delegation used.
Verification: pytest -q openlibrary/catalog/add_book/tests openlibrary/catalog/merge/tests => 84 passed, 8 skipped, 2 xfailed. Ruff check and git diff --check passed.
