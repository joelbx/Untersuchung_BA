# Checkpoint

Task: Add application metadata configuration with a default-enabled `CheckForUpdates` option, loadable from JSON and YAML and integrated with existing config validation.

Status: Implemented `metadata.check_for_updates` in the config model and Viper loader. The default is enabled; an explicit false value is covered in YAML and JSON loader tests. Existing config validation remains in the normal load path.

Verification: `go test ./config` passes. `git diff --check` passes.
