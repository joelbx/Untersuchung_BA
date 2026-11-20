The backup feature is absent, so this needs implementation across several paths rather than a fix to one function:

- [conf/configuration.go](/app/conf/configuration.go:17) defines `conf.Server`, creates startup directories, and validates scan schedules. It is the likely place for `Backup` settings, backup directory creation, duration normalization, and startup rejection of invalid schedules.
- [db/db.go](/app/db/db.go:28) defines `DB` and opens separate SQLite read and write pools. It needs the three public methods; a new `db/backup.go` would hold online backup, restore, and timestamp based pruning.
- [cmd/root.go](/app/cmd/root.go:61) starts scheduled work, while a new `cmd/backup.go` would register the manual commands and confirmations.

I found no existing backup implementation or tests for these behaviors. The main implementation uncertainty is how restore should coordinate with the open database connections; that needs verification before replacing database content. The fix should cover manual backup regardless of retention count, guarded restore and zero count pruning, and automatic backup plus pruning only when all three scheduling settings enable it.

I updated [checkpoint.md](/app/.codex-role-output/checkpoint.md). Project source and tests remain unchanged because this assignment was constrained to fault localization.