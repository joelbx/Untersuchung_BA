# Checkpoint

Implemented the hosts blocking fix in `qutebrowser/components/hostblock.py` and the `widened_hostnames` interface in `qutebrowser/utils/urlutils.py`.

Blocking now checks the global/per-URL toggle first, returns early for whitelisted request URLs, widens the request hostname through parent domains, and compares normalized trailing-dot variants against both runtime and config host sets. Bare hostname `QUrl` inputs are also handled because Qt stores them as paths.

Added helper edge case coverage and blocker regression coverage for parent/subdomain matches, full URLs, trailing dots, whitelist precedence, and both host sets. Updated the existing per-URL toggle test to add a literal host entry.

Verification: `python -m pytest -q tests/unit/utils/test_urlutils.py tests/unit/components/test_hostblock.py` — 357 passed, 1 skipped. `git diff --check` passed before the final bare-host fallback adjustment; rerunning it now.
