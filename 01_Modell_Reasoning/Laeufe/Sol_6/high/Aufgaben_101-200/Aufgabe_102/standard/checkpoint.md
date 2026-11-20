# Checkpoint

- Task: add Linux locally reachable (scope host) IP range facts for IPv4 and IPv6.
- Status: implemented the Linux ``locally_reachable_ips`` fact and focused unit coverage; final review complete.
- Constraints: local repository and existing tests only; preserve the fact workflow and schemas.
- Verification: 146 passed, 5 skipped in the network, fact, and collector unit tests; ``git diff --check`` passed.
