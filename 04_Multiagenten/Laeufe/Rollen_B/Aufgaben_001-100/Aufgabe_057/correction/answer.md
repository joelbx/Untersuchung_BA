Fixed the reviewed attachment issues. YAML string attachments now stay strings in storage; legacy JSON text can be supplied explicitly through `attachment_json`. Export uses a number preserving decode path, with regression coverage for large integers.

`GOPROXY=off go test ./internal/ext ./cmd/flipt` passed.

**TEST_ENVIRONMENT_PROBLEM:** The referenced `internal/ext/testdata` YAML fixtures are absent from this checkout, so exact fixture comparison was unavailable.