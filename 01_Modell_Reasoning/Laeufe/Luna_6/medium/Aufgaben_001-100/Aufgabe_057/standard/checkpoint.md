# Checkpoint

Implemented `internal/ext` YAML import/export support using this checkout's storage and protobuf APIs.

- Export emits flags, variants, rules/distributions, segments, and constraints; variant attachment JSON is decoded into YAML-native values.
- Import creates the same hierarchy and JSON-encodes YAML attachment values for storage, including recursive conversion of YAML map keys.
- Empty/missing attachments are left empty.

Validation: `go test ./internal/ext ./cmd/flipt` passed. This checkout has no `internal/ext/testdata` fixtures or ext tests; those paths described in the issue are not present here.
