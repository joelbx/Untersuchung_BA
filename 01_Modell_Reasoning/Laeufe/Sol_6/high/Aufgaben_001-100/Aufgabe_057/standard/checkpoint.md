Task: implement YAML-native variant attachment import and export in internal/ext.
Status: implemented internal/ext YAML document, importer, exporter, and attachment conversion; CLI import/export now uses the package. Added round-trip and legacy attachment tests.
Verification: GOPROXY=off go test ./... passed; git diff --check passed.
