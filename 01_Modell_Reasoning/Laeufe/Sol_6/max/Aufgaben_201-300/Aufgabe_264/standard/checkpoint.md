Task: Resolve Meraki HTTP 429/500/502 retry handling in /app.
Status: Implemented bounded retries for HTTP 429/500/502, public exceptions, final HTTP status tracking, and rate limit warnings. Failed requests also carry the retry count in their exception text. Added a bugfix changelog fragment and focused unit coverage, including the warning in task output.
Verification: PYTHONPATH=lib:test/units python -m pytest test/units/module_utils/network/meraki -q (17 passed); git diff --check passed.
