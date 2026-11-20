Updated `format_languages` to resolve two-letter ISO codes and English or native language names to canonical MARC keys, then remove duplicates while preserving first occurrence. Added tests for the reported cases.

Verification: 132 relevant tests passed; Ruff and `git diff --check` passed.