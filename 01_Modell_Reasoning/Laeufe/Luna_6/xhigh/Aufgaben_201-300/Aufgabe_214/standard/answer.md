Implemented external `nmap` scanning per server, with native scanning retained when no external scanner path is configured. Added technique mapping, configuration and capability validation, nmap result parsing, and a commented `portscan` example in the discover template.

`GOPROXY=off go test ./config ./scanner ./subcmds` passes. The cgo build prints an existing `go-sqlite3` compiler warning; `git diff --check` passes.

Key files: [config/portscan.go](/app/config/portscan.go), [scanner/portscan.go](/app/scanner/portscan.go), [config/config.go](/app/config/config.go), [subcmds/discover.go](/app/subcmds/discover.go).