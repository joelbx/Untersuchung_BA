Implemented native SQLite backups in the checked-out repository. Configuration now supports `backup.path`, `backup.schedule`, and `backup.count`; the CLI provides `backup create`, `backup prune`, and `backup restore --backup-file`, with confirmation for destructive actions. Scheduled backups also prune files to the configured count.

Added focused tests, and `go test ./...` passes.