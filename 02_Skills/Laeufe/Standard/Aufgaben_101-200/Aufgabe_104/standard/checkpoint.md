# Checkpoint

Task: add metadata configuration with a default-enabled `CheckForUpdates` preference, supported by JSON/YAML loading and validation.

Status: added `Config.Metadata.CheckForUpdates`, defaulting to true, and wired `metadata.check_for_updates` into Viper loading. Added YAML and JSON coverage, plus a documented default in `config/default.yml`.

Checks: `GONOSUMDB='*' GOPROXY=off go test ./config` passed; `GONOSUMDB='*' GOPROXY=off go test ./...` passed after the final fixture adjustment. The full suite emitted a compiler warning from the existing `go-sqlite3` dependency. `rg` is unavailable, so searches used `find` and `grep`.
