# Checkpoint

Task: add application metadata configuration, including a startup version-check preference defaulting to enabled, with JSON/YAML loading and existing validation integration.

Implemented the metadata configuration field and its enabled-by-default value. Added Viper loading for both snake_case and camelCase forms, updated the configuration example, and added YAML and JSON loading coverage. `gofmt` completed and `go test ./config` passed.
