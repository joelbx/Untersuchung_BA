# Checkpoint

Implemented in `lib/ansible/module_utils/network/meraki/meraki.py`:
- Added `HTTPError`, `RateLimitException`, and `InternalErrorException` public exceptions.
- `request()` retains the most recent HTTP status, retries 429/500/502 up to five times with bounded exponential delays, warns when 429 retries occurred, and raises the matching exception when retries are exhausted.
- Other HTTP statuses >= 400 raise `HTTPError` immediately.

Verification: `pytest -q test/units/module_utils/network/meraki/test_meraki.py` completed with 4 passed and 2 failed. The failures are existing assertions for the previous behavior: a 404 must return without raising and a 429 must return without retrying. Those assertions conflict with the requested issue behavior. `git diff --check` passed.
