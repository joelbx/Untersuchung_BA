Implemented native database backups in `/app`.

- Added `backup.path`, `backup.schedule`, and `backup.count` configuration, including startup directory creation and schedule validation.
- Added SQLite online backup and restore methods, plus pruning that keeps the newest timestamped backup files.
- Added `backup create`, `backup prune`, and `backup restore` commands. Pruning with a count of zero and restores require confirmation unless `--force` is used.
- Scheduled automatic backups and pruning when all required settings are configured.

Verification: `go test ./...` passed, and `git diff --check` reported no issues.