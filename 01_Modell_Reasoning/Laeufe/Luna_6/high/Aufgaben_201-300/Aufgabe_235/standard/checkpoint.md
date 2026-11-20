# Checkpoint

Implemented normalized author name construction and alternate-script lookup for MARC 100, 700, and 720 authors. The lookup scans every linked 880 field, normalizes its name, and removes duplicate alternate names. Organization (110) and event (111) parsing remains unchanged.

Updated the existing parser expectation fixtures affected by the required name normalization and newly populated alternate names.

Verification: `pytest -q openlibrary/catalog/marc/tests/test_parse.py` passed (59 passed). `git diff --check` passed.
