# Checkpoint

- Task: make hosts-based blocking cover parent domains and subdomains, with toggle and whitelist overrides.
- Initial state: clean checkout; blocking logic is in `qutebrowser/components/hostblock.py`; hostname widening exists privately in config utils.
- Implemented `urlutils.widened_hostnames` with the specified edge cases.
- Host blocker now checks the per-URL toggle, then whitelist, then every request host suffix against both blocked sets; trailing dots are normalized during file ingestion and handled for in-memory entries.
- Added tests for hostname widening, subdomain blocking from both sets, whitelist precedence, and trailing-dot entries. Corrected an existing toggle test to use a URL with a real host.
- Verification: 439 passed, 1 skipped across hostblock, urlutils, and configutils tests; after the final trailing-dot lookup change, hostblock tests passed 52 passed, 1 skipped. `git diff --check` passed.
