# Checkpoint

Task: Normalize two-letter codes and English/native language names in `format_languages`, and deduplicate canonical language keys in first-seen order.

Status: Implemented normalization using stored ISO identifiers, the existing MARC alias resolver, and stored English/native names. Validated canonical keys and deduplicated in first-seen order. Added mock-site tests for codes, names, mixed duplicates, unknown values, and ambiguous names.

Verification: `pytest -q openlibrary/tests/catalog/test_utils.py openlibrary/catalog/add_book/tests/test_add_book.py` passed (193 tests). `ruff check` and `git diff --check` passed. The repository's current Ruff formatter configuration would reformat pre-existing quote style throughout both files, so no broad formatting rewrite was applied.
