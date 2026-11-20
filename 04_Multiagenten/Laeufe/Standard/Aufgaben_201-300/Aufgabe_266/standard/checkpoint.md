Task: implement local staged or pending import_item lookup by source-prefixed identifiers.
Status: complete. Added STAGED_SOURCES and ImportItem.find_staged_or_pending; Edition.from_isbn uses it for ISBN-13 and ISBN-10. Added SQLite-backed coverage for default/custom sources, both statuses, filtering, and empty identifiers.
Verification: pytest -q openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py --reruns 0 (16 passed); ruff check and git diff --check passed.
