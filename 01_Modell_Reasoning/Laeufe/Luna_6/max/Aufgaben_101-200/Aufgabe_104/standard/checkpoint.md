# Checkpoint

## Issue
Add application metadata configuration with a `CheckForUpdates` preference, defaulting to enabled and loadable from supported config files.

## Progress
- Located the Go configuration loader and its existing tests in `config/config.go` and `config/config_test.go`.
- Added `Metadata.CheckForUpdates` with an enabled default and Viper loading for snake case YAML keys and camel case JSON keys.
- Added YAML and JSON loading fixtures, updated the default config examples, and verified the default remains enabled when metadata is omitted.
- `go test ./config` passes; `git diff --check` passes.
