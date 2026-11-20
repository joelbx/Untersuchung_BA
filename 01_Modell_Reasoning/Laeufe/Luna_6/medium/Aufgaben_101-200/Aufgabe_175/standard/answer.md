Implemented native database backups in `/app`: SQLite backup, restore, and pruning methods; `backup.path`, `backup.schedule`, and `backup.count` configuration; periodic backup scheduling; and the `backup create`, `backup prune`, and `backup restore` CLI commands.

Verification passed: `go test ./...` and `git diff --check`. The checkpoint is at `.codex-role-output/checkpoint.md`.