Implemented alternate-script author parsing for MARC 100, 700, and 720 fields. Names are normalized, linked 880 names are collected without duplicates, and the existing author fields are retained. Binary and XML linkage lookup are supported; organization and event parsing remains unchanged.

Updated existing expected-output fixtures for alternate names and trailing-period removal.

Verification: `pytest -q openlibrary/catalog/marc/tests/test_parse.py` — **59 passed**. `git diff --check` passed.