Updated [wordpress.go](/app/detector/wordpress.go) to map WPScan Enterprise description, CVSS metrics, PoC, and introduced version; preserve the first CVE reference; and normalize timestamps to UTC. Optional metadata is initialized as an empty map when those values are absent.

Validation passed: `go test ./detector`.