# Checkpoint

Task: add metadata configuration with CheckForUpdates defaulting to enabled.
Status: implemented and verified.
Changes: Config.Metadata.CheckForUpdates defaults to true; Viper loads metadata.check_for_updates from YAML/JSON; default sample and fixtures updated.
Tests: go test ./config ./cmd/flipt passed.
