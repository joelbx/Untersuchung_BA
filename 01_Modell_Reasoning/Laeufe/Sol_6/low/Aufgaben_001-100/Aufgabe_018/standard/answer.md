Updated configuration decoding so scalar strings for `[]string` fields split on whitespace, including repeated spaces, tabs, and newlines. Empty strings decode to an empty slice. The same behavior now applies to empty ENV values, and YAML sequences remain unchanged.

Added regression coverage for YAML and ENV inputs, and updated the advanced config fixture. `go test ./internal/config` passes.