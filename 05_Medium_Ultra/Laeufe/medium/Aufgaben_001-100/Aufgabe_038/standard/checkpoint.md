Task: Add transparent gzip response decoding to urls utilities, uri, and get_url.
Status: implemented and verified.
Changes: GzipDecodedReader; Request/open_url/fetch_url/fetch_file decompression controls; module options and documentation; gzip dependency warning/error handling; updated focused URL tests.
Verification: PYTHONPATH=lib python -m pytest -q --reruns 0 test/units/module_utils/urls (84 passed); git diff --check (clean).
