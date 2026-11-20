VERDICT: FIX

**Code defects:** [importer.go](/app/internal/ext/importer.go:71) stores YAML string attachments such as `"123"` and `"true"` as JSON numbers and booleans, changing their type. Encode YAML strings as JSON strings, with an explicit way to identify legacy JSON text. [exporter.go](/app/internal/ext/exporter.go:43) decodes JSON numbers into `float64`, which can round large integers before export; use a number preserving decode path.

**Tests:** `GOPROXY=off go test ./internal/ext ./cmd/flipt` exited 0. The `internal/ext` tests passed; `cmd/flipt` has no test files.

**TEST_ENVIRONMENT_PROBLEM:** The referenced `internal/ext/testdata` YAML fixtures are absent from this checkout, so exact fixture comparison was unavailable.