Updated [encoding.go](/app/internal/ext/encoding.go) to use the YAML v3 decoder and ignore one leading `#` line for JSON imports. This lets nested metadata decode into JSON compatible maps and arrays while leaving ordinary YAML and JSON decoding intact.

Verification: `go test ./internal/ext` passed.