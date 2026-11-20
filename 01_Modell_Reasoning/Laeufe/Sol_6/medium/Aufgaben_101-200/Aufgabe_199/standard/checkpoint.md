Task: migrate openlibrary/catalog/get_ia.py HTTP access from urllib to requests.
Status: complete.
Changes: requests.get with status validation, retry handling, headers and kwargs; Response content/text access; UTF-8 default when no charset; range headers; XML parsing from response content. Updated deprecated marc_subject callers and get_ia tests.
Verification: pytest -q openlibrary/tests/catalog/test_get_ia.py (50 passed); git diff --check passed.
Constraints followed: local code/tests only; no git history or index baseline changes.
