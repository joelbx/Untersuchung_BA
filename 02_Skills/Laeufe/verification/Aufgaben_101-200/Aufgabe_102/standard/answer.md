Added the Linux `ansible_facts.locally_reachable_ips` fact with IPv4 and IPv6 lists from the local routing table. Entries are normalized, deduplicated, and sorted. Unavailable queries return an empty list with a warning. I also documented the fact and added unit tests.

Verification: 146 passed, 5 skipped.