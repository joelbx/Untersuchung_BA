# Checkpoint

Task: restore legacy `listenPorts` JSON compatibility and structured scan port state.
Status: complete.

Changes:
- `AffectedProcess.ListenPorts` accepts legacy string arrays; `ListenPortStats` carries structured scan state.
- Added `PortStat`, `NewPortStat`, and `Package.HasReachablePort`.
- Migrated scan destination selection, reachability tracking, scan collection, and report display to the new fields.
- Added model regression tests and updated existing scan tests for the new representation.

Verification:
- RED: `GOPROXY=off go test ./models -run 'TestLegacyListenPortsUnmarshal|TestNewPortStat|TestHasReachablePort' -count=1` failed because the new API was absent.
- RED: `GOPROXY=off go test ./models -run TestNewPortStat -count=1` failed on a nonnumeric port before validation was added.
- GREEN: focused model and scan/report tests passed.
- GREEN: `GOPROXY=off go test ./...` passed across all packages. A warning from bundled sqlite3 C code appeared during compilation; it did not fail the test run.
- `git diff --check` passed.
