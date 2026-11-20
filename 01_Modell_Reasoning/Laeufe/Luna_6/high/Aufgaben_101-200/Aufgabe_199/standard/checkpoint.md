# Checkpoint

Task: migrate `openlibrary/catalog/get_ia.py` HTTP operations from urllib to requests, preserving behavior while updating response content/text handling and HTTP errors.

Plan:
1. Inspect the implementation and its existing tests.
2. Replace urllib request/response handling with requests, including headers, status validation, and response decoding.
3. Run the relevant existing tests and review the diff.
