Implemented string-to-`[]string` decoding that splits on whitespace and commas, while leaving non-string sources unchanged. Updated the existing config fixture to cover repeated spaces, tabs, newlines, and trimming; its tests exercise both YAML and environment loading.

Validation passed: `go test ./internal/config` and `git diff --check`.