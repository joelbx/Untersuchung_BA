Task: migrate openlibrary/catalog/get_ia.py HTTP access from urllib to requests.
Completed: get_ia.py uses requests.get, status validation, requests exceptions, response content/text, UTF-8 fallback, and Range headers. Updated deprecated marc_subject.py consumers for Response objects. Updated and extended existing tests to use response-like objects and cover retries, terminal HTTP errors, headers/kwargs, decoding, range/truncation, and XML content parsing.
Verification: python -m pytest openlibrary/tests/catalog/test_get_ia.py -q (47 passed); git diff --check passed.
