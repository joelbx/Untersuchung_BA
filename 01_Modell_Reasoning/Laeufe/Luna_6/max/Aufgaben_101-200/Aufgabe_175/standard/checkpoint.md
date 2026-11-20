# Backup support implementation checkpoint

Implemented:
- Added `backup.path`, `backup.schedule`, and `backup.count` configuration, startup directory creation, duration normalization, and cron validation.
- Added SQLite online backup and restore methods, integrity/source-path checks, and timestamp-ordered retention pruning.
- Added `backup create`, `backup prune`, and `backup restore` CLI commands with required confirmations and `--force` overrides.
- Registered scheduled backup plus pruning when path, schedule, and positive retention are configured.

Verification:
- `go test ./...` passed.
- `go test ./db ./conf ./cmd` passed after final edits.
- `git diff --check` passed.
