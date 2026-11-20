Implemented backward-compatible port handling. `AffectedProcess.ListenPorts` now accepts legacy string arrays, while structured reachability data uses `ListenPortStats []PortStat`. Added `NewPortStat` and `Package.HasReachablePort` in [packages.go](/app/models/packages.go:177).

Updated scanning to deduplicate destinations, expand wildcard binds using server IPv4 addresses, and populate reachability stats. Reports now display both legacy strings and structured stats.

Verification passed: `go test ./models ./scan ./report`, `go test ./...`, and `git diff --check`.