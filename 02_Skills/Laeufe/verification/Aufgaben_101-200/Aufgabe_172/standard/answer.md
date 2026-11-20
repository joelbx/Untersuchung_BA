Updated the model so legacy `listenPorts` string arrays parse, while scanning uses `ListenPortStats []PortStat`. Added `NewPortStat` and `HasReachablePort`, and updated destination selection, reachability checks, and report display. Added regression tests for legacy JSON and port handling.

Verification: `GOPROXY=off go test ./models ./scan ./report` passed; `git diff --check` passed.