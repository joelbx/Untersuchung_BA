# Checkpoint

Task: Add Amazon edition language extraction to `serialize(product)` and retain `languages` in cleaned metadata.

Completed: The serializer now reads edition language display values, filters entries marked `Original Language`, removes duplicates while retaining order and exact display text, and adds `languages` only when non-empty. The metadata cleaner now accepts `languages`.

Verification: `pytest -q openlibrary/tests/core/test_vendors.py` passed (33 tests). `git diff --check` passed.
