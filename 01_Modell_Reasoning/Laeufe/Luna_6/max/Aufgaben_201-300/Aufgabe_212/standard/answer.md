Updated [detector/wordpress.go](/app/detector/wordpress.go:36) to preserve WPScan Enterprise summary, PoC, introduced version, and CVSS data. Conversion now uses the first CVE reference, retains URL order, normalizes timestamps to UTC, initializes optional metadata, and processes response keys deterministically.

Validation passed: `go test ./detector` and `git diff --check`.