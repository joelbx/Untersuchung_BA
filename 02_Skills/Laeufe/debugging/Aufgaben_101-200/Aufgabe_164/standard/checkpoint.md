# Import metadata debugging checkpoint

Status: investigating root cause before changes.
Issue: exported YAML with nested metadata and JSON with one leading `#` header fail import; namespace fields must restore correctly.
Initial tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Root cause evidence: `internal/ext/encoding.go` uses yaml.v2 for import. `Flag.Metadata` and `Variant.Attachment` contain `any` values; nested YAML maps enter these values as interface-keyed maps. `Importer.Import` passes metadata directly to `structpb.NewStruct`, which rejects interface-keyed nested maps. Attachment requires a separate `convert` workaround before JSON marshaling. JSON import uses `json.NewDecoder` directly and rejects a leading `#` line. Namespace object decoding and creation already exist in `common.go` and `importer.go`; tests will guard them.
Hypothesis: using yaml.v3 for import decodes nested mappings with string keys, removing both failures in metadata and attachment. A JSON-only first-line filter can skip exactly one line when its first byte is `#`.
Regression tests added before implementation; targeted test command running: `go test ./internal/ext -run 'TestImport_(NestedMetadataAndNamespace|JSONLeadingComment)$' -count=1`.

Reproduction result: targeted pre-fix test failed as expected: YAML case returned `proto: invalid type: map[interface {}]interface {}`; JSON header case returned `unmarshalling document: invalid character '#' looking for beginning of value`.
Pattern analysis: existing string and object namespace decoding in `common.go` works for YAML and JSON; exporter writes namespace key/name/description. Existing attachment `convert` was a YAML v2 workaround. Both imports share `Encoding.NewDecoder`.
Implementation: YAML import decoder now uses yaml.v3 while YAML export encoder remains v2; JSON decoder skips one first line only when first byte is `#`; attachment JSON marshaling uses the decoded value directly. Regression tests cover nested metadata and arrays, nested attachment, namespace fields, plain JSON, one header, and rejected extra or misplaced comments.
Verification: `go test ./internal/ext -run 'TestImport_(NestedMetadataAndNamespace|JSONLeadingComment)$' -count=1` passed after decoder change. `go test ./internal/ext -count=1` passed after removing conversion. `git diff --check` passed. CLI package test is running.

CLI check `go test ./cmd/flipt -run 'TestImport' -count=1` is still compiling with no output at this point. It has not been counted as passed.

Final verification: `go test ./cmd/flipt -run 'TestImport' -count=1` exited 0 with `? go.flipt.io/flipt/cmd/flipt [no test files]` (compile check only). `go test ./internal/ext -count=1` exited 0. `git diff --check` exited 0. No dependencies were downloaded or external research used.
