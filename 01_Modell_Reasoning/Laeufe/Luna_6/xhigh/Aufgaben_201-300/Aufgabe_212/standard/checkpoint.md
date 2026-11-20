# Checkpoint

Issue: support enriched WPScan Enterprise fields in WordPress vulnerability ingestion.

Implementation in `detector/wordpress.go` now parses summary, PoC, introduced version, and CVSS; uses only the first CVE reference for the canonical record ID; preserves WPScan source type, references, classification, and fix status; normalizes publication/update timestamps to UTC; and initializes optional metadata as an empty map when none is supplied.

Verification: `go test ./detector` passed (`ok`, 0.014s). `git diff --check` passed. The only tracked code change is `detector/wordpress.go`.
