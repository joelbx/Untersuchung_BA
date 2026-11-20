# Configuration metadata work

Task: add metadata configuration with a `CheckForUpdates` preference, defaulting to enabled, supported by JSON/YAML loading and existing validation.

Progress: added `Config.Metadata.CheckForUpdates`, defaulted it to `true`, and loaded `metadata.check_for_updates` through Viper. Documented the setting in the default and local YAML examples. Added YAML and JSON fixture coverage and checked JSON served by `/meta/config`.

Verification: `GOPROXY=off GOSUMDB=off go test ./config` passed; `GOPROXY=off GOSUMDB=off go test ./cmd/flipt` built successfully; `git diff --check` passed.

Scope finding: no startup update checker currently exists in the repository, so this change provides its configuration preference without adding a new checker.
