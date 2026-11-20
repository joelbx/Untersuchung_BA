Updated [format_languages](/app/openlibrary/catalog/utils/__init__.py) to resolve ISO 639-1 codes and English or native names to canonical MARC language keys, then remove duplicates while preserving first occurrence. Added regression cases in [test_utils.py](/app/openlibrary/tests/catalog/test_utils.py).

Verification: 186 relevant tests passed; Ruff lint and `git diff --check` passed.