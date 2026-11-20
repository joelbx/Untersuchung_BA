Implemented unified rule segment support for string and `{keys, operator}` YAML formats, including validation, single key `OR_SEGMENT_OPERATOR` fallback, canonical object exports, and updates to snapshot and SQL persistence handling.

Updated the requested export and readonly fixtures and added `import_rule_multiple_segments.yml`.

Verification passed: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql/...` and `git diff --check`.