Added a dedicated `KEVs` field to vulnerabilities, with CISA and VulnCheck detail types. KEV data now populates that field; the scan summary counts CVEs with KEV entries, and JSON output sorts entries by source and vulnerability name.

Existing and focused tests passed with `go test ./models ./detector`.