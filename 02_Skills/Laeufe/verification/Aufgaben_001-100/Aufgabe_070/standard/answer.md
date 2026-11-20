Updated `format_languages` to resolve ISO-639-1 codes and English or native language names to canonical MARC keys. It now removes duplicates while preserving the first occurrence. I added tests for those cases and made the catalog tests set up their language records explicitly.

Verification: 145 relevant tests passed; Ruff and `git diff --check` passed.