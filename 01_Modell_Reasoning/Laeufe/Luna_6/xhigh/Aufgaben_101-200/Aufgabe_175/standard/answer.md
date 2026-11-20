Implemented native SQLite backup support.

- Added `conf.Server.Backup` settings, schedule validation and duration normalization, and startup creation of the backup directory.
- Added online backup, integrity-checked restore, and timestamp-based pruning to the DB interface and implementation.
- Added scheduled backups with retention pruning, plus `backup create`, `backup prune`, and `backup restore --backup-file` commands with the requested confirmations and `--force` flags.

The implementation is in [db/backup.go](/app/db/backup.go), [cmd/backup.go](/app/cmd/backup.go), [conf/configuration.go](/app/conf/configuration.go), and [cmd/root.go](/app/cmd/root.go).

Verification passed: `go test ./db ./conf ./cmd` and `go test ./...`.