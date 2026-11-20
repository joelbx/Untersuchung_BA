Updated the repository so legacy `listenPorts` string arrays parse again. Structured scan ports now use `ListenPortStats` and `PortStat`, with destination selection, reachability updates, and report display using the new fields.

`GOPROXY=off go test ./...` passed. The build emitted a warning from bundled sqlite3 C code.