Updated [MerakiModule.request](/app/lib/ansible/module_utils/network/meraki/meraki.py) to retry HTTP 429, 500, and 502 up to three times, retain the latest status, and warn when rate limiting caused retries. Other HTTP errors raise `HTTPError` immediately. Added the requested exception classes and updated the unit tests.

Verification: all 13 Meraki utility tests passed; `git diff --check` passed.