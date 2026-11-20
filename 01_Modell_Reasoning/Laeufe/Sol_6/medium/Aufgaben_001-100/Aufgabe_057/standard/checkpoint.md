Task: implement YAML-native variant attachment import/export in internal/ext.
Status: complete.
Changes: added shared YAML document types, batched Exporter with JSON-to-YAML attachment decoding, Importer with recursive YAML map-key normalization and JSON attachment encoding; wired CLI commands to new package; added focused hierarchy and attachment round-trip tests.
Verification: go test ./internal/ext ./cmd/flipt ./storage/cache ./server (passed).
Note: the referenced internal/ext/testdata fixtures were not present in this checkout, so fixture byte-for-byte comparison was unavailable.
