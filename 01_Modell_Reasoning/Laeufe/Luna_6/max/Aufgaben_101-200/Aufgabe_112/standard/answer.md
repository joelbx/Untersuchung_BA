Implemented Fortinet CVE detection and enrichment. Fortinet-only CPE matches are retained, advisory IDs and metadata are added to scan results, and confidence is selected across Fortinet, NVD, and JVN. Fortinet is included in report source ordering, and the HTTP handler uses the new enrichment function.

Updated `go-cve-dictionary` to a revision with Fortinet models and detection methods.

**Validation:** Detector, models, and server tests passed using a temporary module file with locally cached compatible dependency versions. The checked-in `go.mod` has no replacements. Offline `go mod tidy` could not resolve uncached transitive versions; no downloads were requested.