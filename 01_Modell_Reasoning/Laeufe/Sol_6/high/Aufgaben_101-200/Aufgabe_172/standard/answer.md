Updated the port model so `vuls report` can parse legacy string `listenPorts` values. New scans use `ListenPortStats` and `PortStat`; destination selection, reachability updates, and report rendering use the new fields while preserving legacy ports. Added `NewPortStat` and `Package.HasReachablePort`.

Verification passed: `GOPROXY=off go test ./models ./scan ./report` and `git diff --check`.