Task: Preserve Amazon edition language metadata through serialization and cleaning.
Status: Complete. Serializer reads ContentInfo.Languages.DisplayValues, excludes Original Language, deduplicates in source order, and omits an empty languages key. Cleaner accepts languages unchanged.
Verification: pytest -q openlibrary/tests/core/test_vendors.py (36 passed); ruff check passed; git diff --check passed. Ruff format --check reports existing repository-wide style differences in both files, so no broad reformat was applied.
Delegation: None.
