Task: implement transparent gzip response handling for urls.py, uri, and get_url.
Status: implementation complete. Added GzipDecodedReader, gzip negotiation/response decoding, decompression options and propagation, missing-gzip handling, and focused tests.
Verification: python -m pytest -q test/units/module_utils/urls (87 passed); git diff --check passed.
Constraints observed: local repository and tests only; git history, index, and harness configuration untouched.
