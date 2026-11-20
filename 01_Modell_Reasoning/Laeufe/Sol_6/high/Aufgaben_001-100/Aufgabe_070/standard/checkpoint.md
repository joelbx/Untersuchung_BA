# Checkpoint

Task: Normalize ISO-639-1 codes and English/native language names to MARC keys in `format_languages`, deduplicating in input order.
Status: Complete.
Changes: Resolve names and two-letter codes with language records, the existing MARC alias map, and Babel English/native names; validate canonical keys and deduplicate. Added regression tests for mixed aliases, recorded native names, an ISO code whose existing alias map is wrong, invalid inputs, and empty inputs.
Verification: 156 add-book tests passed; Ruff and `git diff --check` passed.
