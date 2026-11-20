Added `locally_reachable_ips` to Linux network facts, with separate IPv4 and IPv6 lists drawn from scope-host local routes. Entries are normalized, deduplicated, and consistently ordered. If a query is unavailable, the affected list is empty and fact gathering emits a concise warning.

The network unit tests pass: **10 passed**. No delegation was used.