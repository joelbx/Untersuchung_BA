# Checkpoint

Task: add a Linux fact for locally reachable IP addresses/prefixes (scope host), with deterministic normalized IPv4/IPv6 lists and graceful empty behavior.

Progress: implemented `locally_reachable_ips` in the Linux network collector and registered its fact ID for subset selection. It queries IPv4/IPv6 routes across routing tables with `scope host`, normalizes destinations to canonical prefixes or single IPs, deduplicates and numerically sorts them, and returns empty family lists with warnings when a query fails or reports no usable routes. Existing fact collector and fact platform unit suites passed (136 passed, 5 skipped) via direct pytest. The `ansible-test` wrapper could not start because pytest's `--forked` and `-n` plugins are unavailable. `git diff --check` passed.
