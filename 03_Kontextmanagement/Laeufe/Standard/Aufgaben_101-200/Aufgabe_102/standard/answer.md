Added the Linux `locally_reachable_ips` fact with `ipv4` and `ipv6` lists. It collects host-scope local routes, normalizes and deduplicates entries, and orders them consistently. Failed route queries return an empty list for that family with a warning.

The fact is registered for direct selection. Relevant tests passed: **147 passed, 2 skipped**.