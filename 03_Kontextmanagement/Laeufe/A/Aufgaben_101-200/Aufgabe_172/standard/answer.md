Updated the repository so `AffectedProcess.ListenPorts` accepts legacy string arrays, while scanning uses the new `ListenPortStats []PortStat` field. Added `NewPortStat` and `HasReachablePort`, and updated scan destination selection, reachability matching, and report display for legacy results.

Validation: `GOPROXY=off go test ./...` passed.