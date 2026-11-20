Updated `AffectedProcess` so legacy scan results can load `listenPorts` as strings, while scanning uses `ListenPortStats` and the new `PortStat` API. The report also accepts results containing the earlier structured `listenPorts` objects. Added parsing and JSON regression tests.

`go test ./models ./scan ./report`, `go test ./...`, and `git diff --check` passed. No delegation was used.