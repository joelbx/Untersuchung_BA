# Checkpoint

Implemented YAML-native attachments in the checkout's existing CLI workflow (`cmd/flipt`), because this repository has no `internal/ext` package or supplied ext fixtures. Export parses stored JSON into native YAML-compatible values and reports malformed stored JSON with flag/variant context. Import marshals non-null YAML attachment values back to JSON strings; omitted/null attachments remain empty.

Verification: `go test ./cmd/flipt ./storage/...` passed. The expected `internal/ext/testdata` files are absent in this checkout, so there is no fixture comparison available.
