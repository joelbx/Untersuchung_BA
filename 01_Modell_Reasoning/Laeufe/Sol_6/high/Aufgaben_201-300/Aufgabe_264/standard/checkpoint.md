# Meraki retry issue checkpoint

- Implemented public HTTPError, RateLimitException, and InternalErrorException in the shared Meraki utility.
- Requests retry HTTP 429/500/502 up to three times with 1, 2, and 4 second delays; other HTTP 400+ responses raise immediately.
- Public status tracks the latest response; rate limit retries generate an Ansible warning, and exhaustion includes the retry count in the exception message.
- Updated existing Meraki unit tests for immediate errors, recovery, exhaustion, status, retry count, payload preservation, and warnings.
- Verification: `python -m pytest -q test/units/module_utils/network/meraki/test_meraki.py` (13 passed); `git diff --check` passed.
