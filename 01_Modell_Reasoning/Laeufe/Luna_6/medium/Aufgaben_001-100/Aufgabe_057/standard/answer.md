Implemented YAML-native attachment import/export in the new [internal/ext package](/app/internal/ext/common.go).

Export converts stored attachment JSON into YAML values. Import converts YAML attachment structures into JSON strings and creates flags, variants, segments, constraints, rules, and distributions through the store interfaces. Missing attachments remain empty.

Validation passed: `go test ./internal/ext ./cmd/flipt`. This checkout does not include the referenced `internal/ext/testdata` fixtures or ext tests.