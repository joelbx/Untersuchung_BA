# Checkpoint

Task: Add local staged/pending import lookup by source-prefixed identifier.
Status: Complete.
Changes: Added STAGED_SOURCES and ImportItem.find_staged_or_pending; Edition.from_isbn now checks ISBN-13 and ISBN-10 through it; added lookup tests.
Verification: pytest -q openlibrary/tests/core/test_imports.py (6 passed); git diff --check passed.
