# Checkpoint

Task: Support essential WPScan Enterprise fields in WordPress vulnerability ingestion.

Completed in `detector/wordpress.go`:
- Preserve the first canonical CVE reference per vulnerability and retain the WPScan ID fallback when no CVE is supplied.
- Map description to summary, CVSS score/vector/severity to CVSSv3 model fields, and PoC/introduced version into optional metadata.
- Map publication/update timestamps to UTC and keep references, vulnerability type, source, and fix version mapping.
- Ensure optional metadata is initialized as an empty map when no values are present.

Validation: `go test ./detector` passed.
