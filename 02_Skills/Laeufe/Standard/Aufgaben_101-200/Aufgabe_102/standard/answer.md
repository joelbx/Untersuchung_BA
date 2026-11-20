Added the Linux `locally_reachable_ips` fact with separate IPv4 and IPv6 lists. It collects scope-host routes, normalizes and sorts addresses and prefixes, removes duplicates, and returns empty lists with a warning when a query fails.

Relevant unit tests passed: **153 passed, 7 skipped**. A live route query could not be checked because `ip` is unavailable in this environment.