Updated host blocking so a blocked domain covers its subdomains, including hosts with trailing dots. Whitelisted request URLs return early, and the per-URL blocking toggle still applies. Added `urlutils.widened_hostnames` and regression tests.

Verification: 356 passed, 1 skipped across the hostblock and urlutils test files; the final targeted rerun passed.