Host blocking now checks the request host and each parent domain against both blocked sets. Whitelist rules take precedence, per-URL disabling still applies, and trailing-dot hosts match their non-trailing forms. Added the public `widened_hostnames` helper and regression tests.

Relevant tests: **426 passed, 1 skipped**.