Updated `format_languages` to resolve two-letter codes and language names to canonical MARC keys, then deduplicate results in first-occurrence order. Added a `Deutsch` alias and regression tests for the reported cases.

Verification: all 96 tests in `openlibrary/tests/catalog/test_utils.py` passed.