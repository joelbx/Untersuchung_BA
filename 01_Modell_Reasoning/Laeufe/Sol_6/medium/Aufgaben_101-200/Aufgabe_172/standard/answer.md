Updated the repository so `vuls report` can parse legacy `listenPorts` string lists. Scanning now uses `ListenPortStats` and the new `PortStat`, `NewPortStat`, and `HasReachablePort` interfaces; report rendering also handles legacy ports.

Verification passed: `GOPROXY=off go test ./models ./scan ./report` and `git diff --check`.