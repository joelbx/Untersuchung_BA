Updated `AffectedProcess` so legacy `listenPorts` string arrays decode successfully. New scans use `ListenPortStats` and `PortStat` for destination selection and reachability; report views can display both formats.

Added tests for legacy JSON, port parsing, reachability, and nil-safe updates. `go test -p 1 ./models ./scan ./report` and `git diff --check` pass.