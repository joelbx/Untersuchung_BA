# Checkpoint

Task: resolve WPScan Enterprise field handling in WordPress vulnerability ingestion.

Repository inspection found the mapper in `detector/wordpress.go`. The mapper now emits one result per vulnerability using the first CVE reference, preserves ordered URLs and UTC dates, carries description/classification/fix data, maps CVSS fields, and stores PoC/introduced version in optional metadata. The optional metadata field serializes empty maps as `{}`.

Regression coverage was added for enriched and basic/null payloads. Verification passed: `go test ./detector ./models`.
