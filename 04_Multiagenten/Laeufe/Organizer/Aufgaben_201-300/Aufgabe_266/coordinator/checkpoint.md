# Checkpoint

Task: add local staged/pending import lookup in openlibrary/core/imports.py.
Status: complete. Added STAGED_SOURCES and ImportItem.find_staged_or_pending; ISBN resolution now searches both ISBN forms via the local lookup and retries both forms after import. Added focused tests.
Verification: 17 tests passed in openlibrary/tests/core/test_imports.py and test_models.py; ruff check and git diff --check passed.
Delegation: none.
