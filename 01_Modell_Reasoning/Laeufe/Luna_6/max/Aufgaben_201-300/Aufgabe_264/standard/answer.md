Implemented bounded retries for HTTP 429, 500, and 502 in [meraki.py](/app/lib/ansible/module_utils/network/meraki/meraki.py:363). Persistent errors raise `RateLimitException` or `InternalErrorException`; other HTTP errors raise `HTTPError`. The module retains the latest response status and warns with the retry count when rate limiting occurs.

Updated the focused tests in [test_meraki.py](/app/test/units/module_utils/network/meraki/test_meraki.py:76).

Verification: **9 tests passed**; `git diff --check` passed.