# Checkpoint

Task: Add metadata configuration with a default-enabled CheckForUpdates option, supported by JSON/YAML loading and validation.

Changes: `Config.Metadata.CheckForUpdates` defaults to true and reads `metadata.check_for_updates` through the existing Viper loader. The default YAML example documents the setting. Config tests cover explicit false in JSON and YAML, omitted metadata in both formats, and the JSON response field.

Verification:
- `rg --files -g '!*vendor*'`: unavailable (`/bin/bash: line 1: rg: command not found`); used `find` and `grep`.
- `git diff --check`: passed.
- `GOPROXY=off GOSUMDB=off go test ./config`: passed.
- `GOPROXY=off GOSUMDB=off go test ./...`: passed. Compiler emitted a warning from the existing `github.com/mattn/go-sqlite3` C dependency.
