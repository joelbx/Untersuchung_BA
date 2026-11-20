Implemented configurable per-server nmap scanning with native scanning as the fallback. Added case-insensitive technique mapping and validation, capability checks, nmap output parsing, and the commented config example.

Relevant tests pass: `go test ./config ./models ./scanner ./subcmds`. The build emitted an existing sqlite3 C compiler warning.

Key files: [portscan.go](/app/config/portscan.go:12), [base.go](/app/scanner/base.go:839), [tomlloader.go](/app/config/tomlloader.go:40), and [discover.go](/app/subcmds/discover.go:208).