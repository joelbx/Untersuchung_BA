Resolved the WordPress cache and filtering issues. Cache lookups now use the map directly and treat a present nil value as a miss. The scan uses the per-server `IgnoreInactive` setting to exclude plugins and themes with `Status="inactive"` while keeping active ones.

Tests passed: `go test ./wordpress ./report ./models`.