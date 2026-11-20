# Checkpoint

Task: Fix BSD sysctl fact parsing and uptime collection.
Status: implemented and verified.

- Shared sysctl parsing handles equals, colon, and space delimiters, continuation lines, malformed lines, and command errors with warnings.
- FreeBSD, NetBSD, and OpenBSD collect numeric boot time with `sysctl -n kern.boottime` and calculate uptime seconds.
- Added focused unit tests for parsing, failures, uptime, and hardware fact merging.
- Relevant tests: 14 passed. Full facts suite: 365 passed, 5 skipped, 1 timeout-sensitive failure; that failing test passed in isolation.
