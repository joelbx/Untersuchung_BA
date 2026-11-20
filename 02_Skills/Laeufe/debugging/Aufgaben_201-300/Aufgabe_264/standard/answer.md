Updated [MerakiModule.request](/app/lib/ansible/module_utils/network/meraki/meraki.py) to retry HTTP 429, 500, and 502 up to three times. It now raises the new public exception classes for HTTP errors and retry exhaustion, preserves the final status, and warns when rate limiting caused retries.

Verification: the Meraki unit suite passed (12 tests), and `git diff --check` passed.