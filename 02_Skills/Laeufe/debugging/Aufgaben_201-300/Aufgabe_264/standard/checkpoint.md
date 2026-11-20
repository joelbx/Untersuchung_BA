# Meraki retry investigation

Initial state: working tree clean. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep` for inspection. Investigating request handling and tests before making a fix.

Root cause: `MerakiModule.request` makes one `fetch_url` call, stores `info['status']`, then calls `fail_json` on every status >=300. No retry mechanism exists. `fetch_url` returns `(None, info)` on HTTP errors; current tests mock `fail_json` to no-op and therefore only observe status, masking the immediate failure. Baseline Meraki unit suite: `PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/network/meraki/test_meraki.py` passed (6 tests).

Pattern: neighboring network helpers use bounded loops and `time.sleep`; Meraki call sites route through this single helper. Hypothesis: classifying only 429/500/502 as transient inside `request`, then retrying the same request with a small fixed budget, will preserve normal response decoding while exposing the last status and retry count warning.

Reproduction: Replaced the two status-only tests with exception, retry, and final-status tests. Before the fix, `PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/network/meraki/test_meraki.py` failed at import with `ImportError: cannot import name 'HTTPError'`, confirming the required public interface was absent. The existing single-call request path also lacked retry behavior.

Fix: Added public HTTPError, RateLimitException, and InternalErrorException classes. `request` now retries only 429/500/502 up to three times, with one-second waits, records each response status, warns with the number of rate-limit retries, and raises the appropriate exception on exhaustion. Other >=400 responses raise HTTPError immediately.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/network/meraki/test_meraki.py` passed (12 tests); `git diff --check` passed. No external tooling or downloads used.
