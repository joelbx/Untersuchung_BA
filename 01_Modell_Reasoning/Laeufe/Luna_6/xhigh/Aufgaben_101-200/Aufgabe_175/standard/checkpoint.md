# Checkpoint

## Objective
Implement native SQLite database backup, restore, pruning, CLI commands, configuration, and scheduled backups in `/app`.

## Constraints
- Used local repository code and existing tests only.
- Did not modify git history, the index baseline, or harness configuration.
- Edited checked-out repository files; coordinator exports changes.

## Implemented
- Added nested `conf.Server.Backup` settings for path, schedule, and retention count, with defaults, duration-to-`@every` normalization, schedule validation, and startup directory creation.
- Added online SQLite backup and restore operations to the exported `db.DB` interface and concrete implementation. Restore checks for a regular SQLite file, verifies integrity, and refuses to restore from the live database itself.
- Added timestamped backup naming and timestamp-based pruning, including the internal `prune(ctx) (int, error)` helper.
- Added periodic backup and pruning using the existing scheduler; scheduling is disabled when path/schedule is empty or count is zero.
- Added `backup create`, `backup prune`, and `backup restore --backup-file ...` commands, with the required confirmations and `--force` flags.

## Verification
- `go test ./db ./conf ./cmd` passed.
- `go test ./...` passed across the repository.
- `git diff --check` passed.

## Current repository changes
- Modified: `cmd/root.go`, `conf/configuration.go`, `db/db.go`
- Added: `cmd/backup.go`, `db/backup.go`
