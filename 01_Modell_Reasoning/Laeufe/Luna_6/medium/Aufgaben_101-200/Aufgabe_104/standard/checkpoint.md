# Checkpoint

Implemented metadata configuration in `config.Config` with `CheckForUpdates`, enabled by default. `Load` maps both `metadata.check_for_updates` and the camelCase JSON form (`metadata.checkForUpdates`); YAML coverage uses snake_case and JSON coverage uses camelCase. Existing config tests pass with the defaults and the configured false value.

Verification: `go test ./config` passed.
