# Checkpoint

Issue: restore report compatibility with legacy string-valued `listenPorts`, while using structured port stats in scanning/report destination logic.

Completed:
- Added `PortStat`, `NewPortStat`, and `Package.HasReachablePort`.
- Split legacy `AffectedProcess.ListenPorts []string` from `ListenPortStats []PortStat`.
- Updated Debian/RPM scan collection, destination selection, reachability updates, and report rendering.
- Updated existing scan fixtures to the structured stats API.
- `go test ./models ./scan ./report` passed.
- `go test ./...` passed.
- `git diff --check` passed.
