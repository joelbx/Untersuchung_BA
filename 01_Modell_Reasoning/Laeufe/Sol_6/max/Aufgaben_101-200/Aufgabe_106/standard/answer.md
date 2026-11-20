Updated the WordPress cache to pass the map directly. `searchCache` now returns `("", false)` for a missing key or nil value, while preserving a present empty string.

Scanning and report filtering now honor each server’s `IgnoreInactive` setting and the existing report flag. Packages with `Status="inactive"` are excluded; active packages remain included.

The relevant offline tests passed: `go test ./wordpress ./models ./report`. `git diff --check` also passed.