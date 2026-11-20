Implemented native SQLite backup support.

- Added backup configuration, startup directory creation, duration normalization, and cron validation in [configuration.go](/app/conf/configuration.go:90).
- Added `DB.Backup`, `DB.Restore`, and `DB.Prune`, including SQLite integrity checks and timestamp based retention, in [backup.go](/app/db/backup.go:32).
- Added `backup create`, `backup prune`, and `backup restore` with confirmation safeguards and `--force` in [cmd/backup.go](/app/cmd/backup.go:13).
- Wired scheduled backups and pruning into startup in [root.go](/app/cmd/root.go:157).

Verification passed: `go test ./...`, final focused tests (`go test ./db ./conf ./cmd`), and `git diff --check`.