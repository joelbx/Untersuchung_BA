Task: migrate openlibrary/catalog/get_ia.py HTTP access from urllib to requests.
Status: implemented requests migration, updated deprecated callers, and added HTTP behavior tests. Verified: 47 tests passed in openlibrary/tests/catalog/test_get_ia.py; git diff --check passed.
