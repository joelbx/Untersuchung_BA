Updated the checked-out files so `vuls report` can decode legacy `listenPorts` string arrays. Scanning now uses `ListenPortStats []PortStat`, and reports display either structured ports or legacy strings. Added `NewPortStat`, `HasReachablePort`, and coverage for parsing, reachability, and nil cases.

Verification passed: `go test -p 1 ./models ./scan ./report` and `git diff --check`.