Added per-server `nmap` port scanning with configurable techniques, source port, privilege validation, and XML result parsing. Servers without an external scanner path continue to use the native scanner. The discover template now includes a commented `portscan` example.

`go test ./...` passed. The run emitted an existing `go-sqlite3` C compiler warning.