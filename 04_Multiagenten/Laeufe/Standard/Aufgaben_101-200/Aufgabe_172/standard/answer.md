Updated `AffectedProcess` so legacy `listenPorts` string arrays parse successfully. Structured scan data now uses `ListenPortStats []PortStat`; scanning, reachability checks, and reports use the new field, while reports can still display legacy ports. Added `NewPortStat` and `HasReachablePort`.

Verification passed: `go test ./models ./scan ./report` and `git diff --check`.