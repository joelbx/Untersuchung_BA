# Checkpoint

Task: Refactor `detectScanDest` to group deduplicated, deterministically ordered ports by IP address, update consumers, and run relevant existing tests.

Status: Complete.

- `detectScanDest` now returns `map[string][]string`, expands wildcard listeners to IPv4 addresses, deduplicates ports per address, and sorts each port slice.
- `execPortsScan` consumes the map and sorts addresses before scanning, keeping downstream status updates stable.
- Updated existing destination tests and added a case for multiple ports, duplicate listeners, and wildcard overlap.
- Verification: `GOPROXY=off GOSUMDB=off go test -mod=readonly ./scan` passed; `git diff --check` passed.
