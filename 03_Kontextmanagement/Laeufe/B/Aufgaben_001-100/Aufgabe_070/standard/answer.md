Updated [format_languages](/app/openlibrary/catalog/utils/__init__.py:448) to resolve ISO 639-1 codes and English or native language names to canonical MARC keys, then deduplicate in first-seen order. Unknown or ambiguous names still raise `InvalidLanguage`.

Verification passed: 100 catalog utility tests, 86 add-book tests, focused normalization tests, Ruff, and `git diff --check`.