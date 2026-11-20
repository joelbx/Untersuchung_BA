# Checkpoint

Task: add a metadata configuration section with startup version update preference, defaulting to enabled and supported in JSON/YAML through existing config loading and validation.

Completed:
- Added `metadata.check_for_updates` to the config structure and loader, with `CheckForUpdates` enabled in `Default()`.
- Loader accepts the snake case YAML key and camel case JSON field.
- Added the setting to the sample default YAML and covered default behavior plus disabled preferences in YAML and JSON fixtures.
- Verified with `go test ./config` (pass).
