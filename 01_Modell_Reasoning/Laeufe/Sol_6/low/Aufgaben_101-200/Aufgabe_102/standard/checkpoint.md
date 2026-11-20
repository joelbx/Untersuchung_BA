Task: add locally reachable scope-host IP facts to Linux network collection.
Status: implemented locally_reachable_ips with IPv4/IPv6 local routing table queries, normalization, deduplication, sorting, and warnings on unavailable queries.
Verification: network fact unit tests 7 passed; git diff --check clean.
