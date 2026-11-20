# Checkpoint

Task: Refactor `detectScanDest` to group sorted, unique ports by IP address, update consumers, and run relevant existing tests.

Status: Complete. `detectScanDest` returns a non-nil map of IP addresses to sorted, unique port slices. `execPortsScan` accepts the map and scans IPs in sorted order. Existing destination tests now assert the map format and cover duplicate ports, wildcard overlap, and no available wildcard addresses.

Verification: `GOPROXY=off GOSUMDB=off go test ./scan -count=1` passed. `git diff --check` passed.
