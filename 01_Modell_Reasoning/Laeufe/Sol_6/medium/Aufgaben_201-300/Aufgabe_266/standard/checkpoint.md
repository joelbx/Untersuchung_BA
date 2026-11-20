Task: Add local lookup for staged or pending import items by source and identifier.
Completed: Added STAGED_SOURCES and ImportItem.find_staged_or_pending, then wired Edition.from_isbn to look up both ISBN forms. Added lookup and ISBN import tests.
Verification: pytest -q -o reruns=0 openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py (17 passed); ruff check on changed Python files and git diff --check passed.
