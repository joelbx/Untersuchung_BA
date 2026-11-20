# Checkpoint

Task: migrate HTTP handling in `openlibrary/catalog/get_ia.py` from urllib to requests, update response content handling and errors, and run relevant existing tests.

Initial inspection: repository is at `/app`; `rg` is unavailable, so use standard shell tools for repository discovery. Candidate implementation and tests are `openlibrary/catalog/get_ia.py` and `openlibrary/tests/catalog/test_get_ia.py`.
