# Checkpoint

Task: Fix Meraki API handling for HTTP 429, 500, and 502 with bounded retries, public exception types, and last-response status tracking.

Completed:
- Added HTTPError, RateLimitException, and InternalErrorException.
- Added five bounded retries with a one-second delay for 429, 500, and 502 responses.
- Preserve the most recent response status, raise the appropriate exception after exhaustion, and warn when rate limiting caused retries.
- Updated focused unit tests for immediate HTTP errors, successful retries, and exhausted retries.

Verification: `python -m pytest -q test/units/module_utils/network/meraki/test_meraki.py` (9 passed); `git diff --check` passed.

Constraints respected: Used only checked-out repository code and existing tests. No downloads, delegation, git history changes, index baseline changes, or harness configuration changes.
