Task: Support WPScan Enterprise fields in WordPress vulnerability ingestion.
Status: Complete. Updated detector/wordpress.go to map description, poc, introduced_in, CVSS v3 fields, UTC timestamps, and first CVE identifier while retaining WPScan fallback IDs. Added regression coverage for enriched, null, and omitted fields in detector/wordpress_test.go.
Verification: go test ./detector -count=1 passed; git diff --check passed.
