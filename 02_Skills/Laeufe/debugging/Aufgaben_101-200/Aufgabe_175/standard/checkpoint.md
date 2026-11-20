# Backup issue checkpoint

Investigating repository paths and existing behavior before changes. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find`.

Root cause: `db.DB` only exposes read/write/close; `cmd/root.go` registers no backup commands or scheduling; `conf/configuration.go` has no Backup options. Existing scan scheduling uses `scheduler.GetInstance().Add`, and scan validation uses `cron.New().AddFunc` after converting durations. SQLite driver exposes `SQLiteConn.Backup`/`SQLiteBackup.Step`/`Finish` locally. Hypothesis: wiring these existing patterns to a backup implementation will supply online copies and scheduled retention.

Added a failing regression test before implementation. Initial `GOPROXY=off go test ./db -run TestBackupRestoreAndPrune -count=1` failed with missing `conf.Server.Backup` and `db.Backup`/`Restore`/`Prune`, as expected. Implemented config, CLI, scheduling, SQLite online copy/restore, and timestamp retention. Added duration/invalid schedule tests.

Verification: `GOPROXY=off go test ./db ./conf ./cmd -count=1` passed; `GOPROXY=off go build ./cmd ./db ./conf` passed; `git diff --check` passed. No offline tooling check was blocked. `rg` was unavailable, so repository inspection used `grep`/`find`.
