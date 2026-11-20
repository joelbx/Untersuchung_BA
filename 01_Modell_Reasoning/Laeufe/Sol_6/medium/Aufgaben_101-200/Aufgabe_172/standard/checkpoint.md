Issue: Restore report compatibility with legacy listenPorts JSON.
Completed: AffectedProcess now stores legacy string ListenPorts and structured ListenPortStats; PortStat/NewPortStat/HasReachablePort added. Scan collection, destination expansion, reachability matching, and report rendering updated. Existing scan tests migrated and model compatibility tests added.
Verification: GOPROXY=off go test ./models ./scan ./report passed; git diff --check passed.
