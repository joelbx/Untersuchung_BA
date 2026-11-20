Updated WPScan ingestion to use the first CVE reference as the canonical ID and preserve Enterprise summaries, proof-of-concept and introduced-version metadata, and CVSS metrics. Basic payloads leave optional metadata empty; timestamps are mapped to UTC.

Added tests for enriched, null, and omitted fields. `go test ./detector -count=1` passes.