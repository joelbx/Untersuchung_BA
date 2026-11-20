# Backup implementation checkpoint

Task: add native SQLite backup, restore, pruning, scheduled backups, configuration, and CLI commands.

Implemented:
- Added `backup.path`, `backup.schedule`, and `backup.count` configuration under `conf.Server.Backup`, with startup directory creation and cron/duration validation.
- Added SQLite online backup and restore operations plus timestamp-based retention pruning to `db` and its exported interface.
- Added `backup create`, `backup prune`, and `backup restore` CLI commands with the requested confirmation and `--force` behavior.
- Registered periodic backups and pruning with the existing scheduler, disabled when any required setting is absent or retention is zero.

Verification: `go test ./...` passed across all existing packages.
