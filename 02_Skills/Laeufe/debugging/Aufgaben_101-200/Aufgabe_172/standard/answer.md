Fixed legacy `listenPorts` parsing by restoring `AffectedProcess.ListenPorts` as `[]string` and moving structured scan data to `ListenPortStats []PortStat`. Added `NewPortStat` and `HasReachablePort`, and updated scan and report consumers.

The legacy JSON regression test now passes. `go test ./models ./scan ./report -count=1` and `git diff --check` both passed.