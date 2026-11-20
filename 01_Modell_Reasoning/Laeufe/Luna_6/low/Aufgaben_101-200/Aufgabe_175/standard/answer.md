Implemented native database backup support:

- Added `backup.path`, `backup.schedule`, and `backup.count` configuration, schedule validation, and startup directory creation.
- Added SQLite online backup, restore, and pruning methods to `db.DB`.
- Added `backup create`, `backup prune`, and `backup restore` CLI commands with the requested confirmation behavior.
- Added scheduled backups and pruning when backup settings are enabled.

`go test ./db ./cmd ./conf` passes. No dedicated backup tests existed in those packages.