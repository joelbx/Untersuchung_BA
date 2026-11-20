# Checkpoint

Task: Support essential WPScan Enterprise fields in WordPress vulnerability ingestion.
Status: Complete.
Changes: WPScan conversion maps description, proof of concept, introduced version, and CVSS metrics; uses the first CVE identifier; normalizes timestamps to UTC; keeps an empty optional map for basic responses. Added payload-based coverage for enriched, absent, and null fields.
Verification: `go test ./detector -run 'TestConvertToVinfosWPScanFields|TestRemoveInactive' -count=1` passed; `go test ./detector -count=1` passed; `git diff --check` passed.
Delegation: None.
