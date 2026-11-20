# Checkpoint

Task: map essential and Enterprise WPScan WordPress vulnerability fields into ingestion records.

Changes: `detector/wordpress.go` uses the first CVE reference as the canonical ID, maps Enterprise description, proof of concept, introduced version and CVSS into existing model fields, initializes optional metadata to an empty map, and normalizes timestamps to UTC. `detector/wordpress_test.go` covers enriched, null and omitted fields, reference order, canonical ID, source, classification, fix version, and UTC times.

Verification:
- `go test ./detector -count=1` passed (exit 0).
- `go test ./detector -run 'TestConvertToVinfosWPScanFields|TestConvertToVinfosWPScanOmittedFields' -count=1` passed (exit 0).
- `git diff --check` passed (exit 0).
