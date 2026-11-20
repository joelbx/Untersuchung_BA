Task: migrate openlibrary/catalog/get_ia.py HTTP access from urllib to requests.
Implemented: requests.get with headers and **kwargs, raise_for_status, HTTPError status handling, UTF-8 fallback when no charset, Response content/text callers, Range header, binary XML parsing. Updated deprecated marc_subject callers for Response. Updated fixture and added focused tests.
Verification: pytest -q openlibrary/tests/catalog/test_get_ia.py openlibrary/catalog/marc/tests/test_get_subjects.py: 95 passed. No delegation used.
