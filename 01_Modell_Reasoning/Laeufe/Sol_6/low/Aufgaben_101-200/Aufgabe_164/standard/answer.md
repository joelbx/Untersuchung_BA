Updated the import flow to use YAML v3, preserving nested metadata and attachments in JSON compatible structures. JSON imports now skip one leading line when it starts with `#`. Added coverage for nested metadata, namespace key/name/description, and JSON imports with and without a header.

`go test ./internal/ext` and `git diff --check` pass.