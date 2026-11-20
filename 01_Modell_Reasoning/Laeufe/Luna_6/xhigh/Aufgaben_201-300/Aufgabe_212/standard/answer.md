Updated [wordpress.go](/app/detector/wordpress.go) to preserve WPScan’s first CVE reference, UTC timestamps, ordered reference links, vulnerability type, and fix version. It now maps description, PoC, introduced version, and CVSS into the existing record fields, with empty optional metadata when those fields are absent.

Verification passed: `go test ./detector` and `git diff --check`.