# Work checkpoint

Issue: add configurable external nmap port scanning while preserving native scanning.

Implemented per-server `PortScanConf`, scan technique mapping and validation, TOML activation of the external scanner, nmap execution and grepable output parsing, native fallback, IPv6-safe host formatting, and the commented discover config example.

Validation: `go test ./config ./models ./scanner ./subcmds` passes. `git diff --check` passes. The sqlite3 C compiler emits an existing `-Wreturn-local-addr` warning during test builds.
