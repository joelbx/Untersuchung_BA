Implemented native SQLite backups in `/app`: configurable backup path, schedule, and retention; scheduled backup and pruning; and `backup create`, `backup prune`, and `backup restore` CLI commands with the required confirmations. Backups use SQLite’s online backup API.

Added an integration test for creation, restoration, and pruning. `go test ./...` passes.