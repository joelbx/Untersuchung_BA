# Checkpoint

Task complete: support essential WPScan Enterprise fields in WordPress vulnerability ingestion.

Implementation in `detector/wordpress.go`:
- Preserve the WPScan origin (`models.WpScan` / `wpscan`), first canonical CVE reference, ordered public URLs, UTC timestamps, verbatim vulnerability type, and fixed version.
- Carry summary, PoC and introduced version metadata, and CVSS score/vector/severity. Accept CVSS `severity` or WPScan `rating`.
- Keep optional metadata initialized to an empty map when absent and make conversion deterministic across response keys.

Validation: `git diff --check` and `go test ./detector` passed.
