Implemented whitespace-aware scalar string decoding for `[]string`, preserving comma separation and returning an empty slice for blank input. Updated the config fixture to verify YAML and environment loading, and added hook tests for whitespace, empty values, and unchanged sequences.

`go test ./internal/config` passed.