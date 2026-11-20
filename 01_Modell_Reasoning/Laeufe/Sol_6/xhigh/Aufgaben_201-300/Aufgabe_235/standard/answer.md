Updated [MARC author parsing](/app/openlibrary/catalog/marc/parse.py) to normalize names and dates and import deduplicated alternate names from linked 880 fields for 100, 700, and 720 authors. Added linkage tests and updated affected expectations.

Verification: 130 tests passed, 1 expected failure; `git diff --check` passed.