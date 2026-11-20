# Checkpoint

Task: implement configurable external `nmap` port scanning alongside the native scanner.

Constraints: work from checked-out repository code and existing tests; do not alter git history, index baseline, or harness configuration.

Complete: added per-server TOML configuration, case-insensitive scan technique mapping, configuration and capability validation, local nmap execution and result parsing, native scanner dispatch, and discover template examples. Existing scanner behavior remains the default when no external scanner path is configured.

Verification: `GOPROXY=off go test ./config ./scanner ./subcmds` passes. The cgo build emits an existing `go-sqlite3` compiler warning. `git diff --check` passes.
