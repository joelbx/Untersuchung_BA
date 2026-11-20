# Checkpoint

Task: Add a dedicated Linux network fact for IP addresses and prefixes marked `scope host`, normalized, deduplicated, and consistently ordered for IPv4 and IPv6.

Implemented `LinuxNetwork.get_locally_reachable_ips(ip_path)` and integrated its `locally_reachable_ips` result into Linux network facts. Registered the fact with the network collector so fact filtering recognizes it. The method queries host-scope routes in all tables, canonicalizes destinations, and sorts/deduplicates each address family. Missing `ip`, unsupported IPv6, failed queries, and empty route results return empty lists with concise warnings without stopping other fact gathering.

Validation: `git diff --check` passed. Relevant existing unit selection passed: 141 passed, 5 skipped.
