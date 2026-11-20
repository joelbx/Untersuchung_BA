Implemented WPScan Enterprise field handling in [wordpress.go](/app/detector/wordpress.go). Records now use the first CVE reference, preserve ordered URLs and UTC timestamps, and carry the summary, classification, fix version, CVSS metrics, and optional PoC and introduced version. Empty optional metadata serializes as `{}`.

Added regression coverage for enriched and basic payloads in [wordpress_test.go](/app/detector/wordpress_test.go).

Verified with `go test ./detector ./models`; `git diff --check` also passed.