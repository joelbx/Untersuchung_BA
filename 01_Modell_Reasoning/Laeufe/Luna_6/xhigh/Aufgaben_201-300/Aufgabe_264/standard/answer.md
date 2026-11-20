Implemented bounded retries for Meraki API responses 429, 500, and 502 in [meraki.py](/app/lib/ansible/module_utils/network/meraki/meraki.py). Exhausted retries raise `RateLimitException` or `InternalErrorException`; other HTTP errors raise `HTTPError` immediately. The module retains the latest response status and warns with the retry count when rate limiting occurs.

Added coverage for immediate HTTP errors, rate limit recovery and exhaustion, and server error retries in [test_meraki.py](/app/test/units/module_utils/network/meraki/test_meraki.py).

Verification: **9 tests passed** with the focused pytest run; `git diff --check` passed. `ansible-test` skipped because this checkout supports Python only through 3.8, while Python 3.11 is available.