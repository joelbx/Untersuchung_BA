Implemented legacy `listenPorts` compatibility and structured port reachability across scanning and reporting. Added `PortStat`, `NewPortStat`, and `HasReachablePort`; updated scan destination selection, wildcard expansion, and report rendering.

Verification passed: `go test ./models ./scan ./report` and `git diff --check`.