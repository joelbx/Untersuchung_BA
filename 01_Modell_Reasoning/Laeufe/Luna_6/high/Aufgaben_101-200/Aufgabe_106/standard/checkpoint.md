# Checkpoint

Completed the WordPress cache and package filtering fix.

- Cache lookup operates directly on `map[string]*string`; missing keys and nil values return `"", false`.
- `FillWordPress` receives the ignore-inactive choice from the per-server WordPress configuration.
- The inactive filtering helper excludes `Status == "inactive"` and preserves active packages; existing tests cover this behavior.
- Added a cache test for a key whose value is nil.

Validation passed: `go test ./wordpress ./report` and `git diff --check`.
