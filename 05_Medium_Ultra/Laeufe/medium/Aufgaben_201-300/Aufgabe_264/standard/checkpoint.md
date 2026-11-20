Task: Add bounded retries for Meraki HTTP 429/500/502, public exceptions, status tracking, and rate-limit warnings.
Status: Implemented and verified in checked-out files.
Implementation: request() retries HTTP 429/500/502 up to three times with one-second waits; raises RateLimitException or InternalErrorException on exhaustion, HTTPError immediately for other HTTP >=400 statuses. Tracks the last status and warns with the number of rate-limit retries. Exhausted rate-limit exceptions also include the retry count.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/network/meraki/test_meraki.py (12 passed); git diff --check passed.
