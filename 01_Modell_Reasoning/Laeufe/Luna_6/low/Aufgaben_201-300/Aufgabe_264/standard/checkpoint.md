# Meraki HTTP retry issue

- Inspect the shared Meraki request helper and current unit tests.
- Add bounded retries for HTTP 429, 500, and 502; preserve status on each request and raise the specified exception types when retry budget is exhausted.
- Existing targeted tests: `python -m pytest -q test/units/module_utils/network/meraki/test_meraki.py` (7 passed).
- Implementation raises `HTTPError` for other HTTP status codes >= 400; retries 429/500/502 up to five times with one-second delays; raises a specific exhaustion exception and warns with retry count for 429.
