Task: implement YAML-native variant attachment import/export in internal/ext.
Status: implemented internal/ext document, exporter, importer, conversion and focused tests; CLI commands now use ext.
Verification: go test ./storage/sql/... ./internal/ext ./cmd/flipt passed; git diff --check passed.
Delegation: none.
Constraints: local code/tests only; preserve git index/history and harness configuration.
