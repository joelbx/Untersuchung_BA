Added a dedicated `KEVs` field to vulnerabilities and populated it from CISA and VulnCheck records, including source specific details and valid due dates. KEV entries now sort consistently, and scan summaries report the number of CVEs with KEV data. The cached go-kev dependency was updated to support VulnCheck.

Verification passed: `go test ./models ./detector ./reporter` and `git diff --check`.