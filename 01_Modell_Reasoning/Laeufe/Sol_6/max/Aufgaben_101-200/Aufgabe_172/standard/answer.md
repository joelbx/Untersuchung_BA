Fixed `vuls report` compatibility with legacy `listenPorts` string arrays. [AffectedProcess](/app/models/packages.go) now keeps those strings separately from structured `PortStat` data and also reads previously saved port objects. Scanning and report views use the structured field.

Verified with `GOPROXY=off GOSUMDB=off go test ./models ./scan ./report`; all passed.