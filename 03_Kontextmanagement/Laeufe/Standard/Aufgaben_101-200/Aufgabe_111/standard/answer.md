Updated Amazon Linux detection so releases 2023, 2025, 2027, and 2029 retain their version instead of falling back to Amazon Linux 1. Added EOL mappings and tests for version normalization, unknown releases, and support end boundaries.

`go test ./config ./scanner` passes with module downloads disabled.