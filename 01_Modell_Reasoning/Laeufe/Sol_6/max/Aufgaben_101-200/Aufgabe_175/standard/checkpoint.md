# Backup implementation checkpoint

- Goal: add native SQLite backup, restore, pruning, CLI commands, and scheduled backups.
- Current state: implemented backup configuration, scheduled backup and retention, SQLite online backup and restore, and CLI create/prune/restore commands.
- Safety: destructive CLI actions require confirmation unless forced; restore validates its source; backups publish only after a successful copy.
- Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./...` passed; `go run . backup --help` lists all commands.
