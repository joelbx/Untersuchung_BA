# Checkpoint

Task: Resolve the flag import bug described in the issue.

Constraints: Work from the checked-out repository and existing tests. Preserve valid YAML and JSON import behavior; support YAML v3 decoding, JSON files with one initial `#` comment line, nested metadata, and namespace key/name/description fields.

Progress: Starting repository inspection. No implementation changes yet.

Implementation progress:
- YAML decoders now use yaml.v3; custom union unmarshallers use the v3 node API.
- JSON decoding skips exactly one initial line when it begins with `#`.
- Removed attachment map conversion; YAML v3 mappings can be marshalled directly as JSON.
- Next: run existing `internal/ext` tests and review the resulting diff.

Verification:
- `go test ./internal/ext` passed (`ok`, 0.068s), covering existing import and export tests for JSON and YAML.
- `git diff --check` passed.
- No test files or harness configuration were changed.
