# Checkpoint

Implemented per-server external nmap scanning with TOML configuration, scan technique mapping, validation, capability checks for non-root privileged scans, XML result parsing, and native scanner fallback. Added commented discover template examples and focused config/scanner tests.

Verification (2026-10-29):
- `GOPROXY=off go test ./config ./scanner ./subcmds` — exit 0.
- `GOPROXY=off go test ./...` — exit 0; all packages passed or had no tests. The pre-existing sqlite3 C compiler warning appeared during compilation.
- `git diff --check` — exit 0.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`.
