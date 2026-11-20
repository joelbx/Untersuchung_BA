Issue: restore legacy listenPorts JSON compatibility while retaining structured scanning data.
Implemented: AffectedProcess.ListenPorts []string and ListenPortStats []PortStat; PortStat/NewPortStat/HasReachablePort; compatibility decoder for prior object listenPorts; scanning, destination selection, reachability, and report rendering updated. Existing scan tests migrated to the new API; added JSON regression tests.
Verification: go test ./models ./scan ./report passed; go test ./... passed; git diff --check passed. The Go build emitted a non-fatal warning from the existing sqlite3 dependency.
Delegation: none.
