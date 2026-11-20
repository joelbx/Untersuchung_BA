# MARC alternate-script author import

Completed author name normalization and linked 880 extraction for person fields 100, 700, and 720. Added XML linkage tests and updated affected binary MARC expectations.

Verification: `pytest -q openlibrary/catalog/marc/tests openlibrary/catalog/merge/tests/test_merge_marc.py` passed (130 passed, 1 expected failure). `git diff --check` passed.
