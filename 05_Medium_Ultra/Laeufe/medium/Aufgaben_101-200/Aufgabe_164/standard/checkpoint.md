# Import metadata issue checkpoint

- Switched YAML import decoding to yaml.v3; retained the existing YAML export encoder.
- JSON import skips exactly one first line when its first byte is `#`.
- Removed attachment map conversion; YAML v3 now provides JSON compatible nested maps directly.
- Added regression coverage for nested flag metadata, nested variant attachments, namespace key/name/description, plain JSON, JSON export headers, and strict header position.
- Verification: `go test ./internal/ext ./cmd/flipt` passed (`cmd/flipt` has no test files). `git diff --check` passed.
