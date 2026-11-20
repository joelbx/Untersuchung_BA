# Checkpoint

Task: resolve import failures for exported YAML/JSON containing nested metadata and JSON files with one leading `#` comment line.

Changes:
- Switched YAML encoding/decoding to `gopkg.in/yaml.v3`; updated custom YAML unmarshallers to the v3 node API.
- JSON import skips one initial line only when its first character is `#`.
- Removed the YAML map conversion workaround; nested metadata and attachments now serialize directly because YAML v3 decodes ordinary mappings with string keys.
- Added regression coverage for nested metadata and attachments in YAML and commented JSON, plus namespace key/name/description restoration.

Verification: `go test ./internal/ext` passed; `git diff --check` passed.
