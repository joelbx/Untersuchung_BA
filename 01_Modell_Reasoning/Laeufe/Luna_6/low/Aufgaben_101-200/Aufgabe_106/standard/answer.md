Implemented the WordPress cache and filtering changes.

- Cache lookups now take a map directly and report empty cached values as misses.
- The scanner gets `IgnoreInactive` from the server’s WordPress configuration. Filtering removes packages with `Status="inactive"` and retains active packages.
- Added coverage for an empty cached value.

`go test ./wordpress ./report` passed. The build emitted a pre-existing SQLite compiler warning.