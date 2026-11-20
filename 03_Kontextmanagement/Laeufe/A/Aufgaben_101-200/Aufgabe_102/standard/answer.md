Added `locally_reachable_ips` to Linux network facts. It provides separate IPv4 and IPv6 lists of scope-host addresses and prefixes, normalized, deduplicated, and sorted. Unavailable queries return empty lists with a warning.

The relevant network fact tests pass: **10 passed**. Live route collection was not tested because `ip` is unavailable in this environment.