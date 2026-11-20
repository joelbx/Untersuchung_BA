Updated the result model so `vuls report` can parse legacy `listenPorts` string arrays. Scanning now uses `ListenPortStats` and the new public `PortStat`, `NewPortStat`, and `HasReachablePort` interfaces. Report views also display legacy port strings.

Verification passed: `go test ./models ./scan ./report` and `git diff --check`.