# Checkpoint

Task: restore legacy `listenPorts` JSON compatibility while keeping structured port scanning and reachability.

Status: implemented. `AffectedProcess.ListenPorts` accepts legacy string arrays; `ListenPortStats` holds structured scan data. Added `PortStat`, `NewPortStat`, and `Package.HasReachablePort`; updated Debian/RHEL scan collection, destination selection, reachability updates, and report rendering. Added JSON, parsing, and destination overlap tests.

Verification: `GOPROXY=off GOSUMDB=off go test ./models ./scan ./report` passed. `git diff --check` passed. The Go test command emitted a C compiler warning from bundled sqlite3 code; tests still passed.
