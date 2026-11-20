# Checkpoint

Resolved legacy `listenPorts` decoding by using `AffectedProcess.ListenPorts []string` and `ListenPortStats []PortStat`. Added strict `NewPortStat` parsing and `Package.HasReachablePort`; migrated scan destination and reachability logic to structured stats. Report formatting uses structured stats when present and legacy strings otherwise. Debian and Red Hat collectors populate both fields. Updated existing scan tests and added model tests for legacy JSON, invalid ports, and reachability.

Verification: `GOPROXY=off GOSUMDB=off go test -p 1 ./models ./scan ./report` passed. `git diff --check` passed. The initial parallel Go test invocation encountered a transient standard library import error; serial testing passed.
