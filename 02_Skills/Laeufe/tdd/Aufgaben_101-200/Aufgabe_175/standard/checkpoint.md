# Backup task checkpoint

- Repository inspected; work in progress.
- `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep`.
- Implemented backup configuration, CLI commands, scheduled backup and pruning, and SQLite online backup/restore.
- Added regression tests for WAL round trip, pruning, schedule parsing, confirmation, URI metacharacters, and live database aliases. Watched tests fail before their fixes.
- Final verification: `GOTOOLCHAIN=local GOPROXY=off go test ./...` passed; `git diff --check` passed.
