# Checkpoint

Task: implement YAML-native variant attachment import/export in internal/ext.
Status: complete. Added shared YAML document types, paginated exporter, importer with recursive YAML map conversion, CLI integration, and regression tests for nested/mixed attachments, missing attachments, legacy JSON objects, references, and pagination.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/ext ./cmd/flipt ./storage/... ./server/... passed; git diff --check passed.
Constraints: local code/tests only; git history, index baseline, and harness configuration unchanged.
