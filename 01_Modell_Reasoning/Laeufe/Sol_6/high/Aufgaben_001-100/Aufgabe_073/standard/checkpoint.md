# Checkpoint

Task: Include Amazon edition languages in serialized imports and retain them during metadata cleaning.

Status: Complete. The serializer reads edition language display values, omits Original Language entries, removes duplicates while preserving order, and emits languages only when the list is non-empty. The cleaning helper retains languages.

Verification: `pytest -q openlibrary/tests/core/test_vendors.py` passed (37 tests); `ruff check` passed; `git diff --check` passed. Black is unavailable in this environment. Ruff format suggests broad changes to the repository's existing formatting, so no automatic formatting was applied.
