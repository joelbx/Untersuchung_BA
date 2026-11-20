# Checkpoint

Task: Add Fortinet advisory data as a first-class CVE detection and enrichment source for FortiOS targets.

Completed:
- Updated go-cve-dictionary to the locally cached revision that defines Fortinet advisory models and detection method enums.
- CPE detection now retains Fortinet-only CVEs, records advisory IDs, and selects the highest confidence signal across NVD, JVN, and Fortinet.
- Added `models.ConvertFortinetToModel` and `detector.FillCvesWithNvdJvnFortinet`; scanner and HTTP enrichment call the new function.
- Added Fortinet content type, report metadata/source handling, and requested title, summary, and CVSS selection order.

Validation:
- `git diff --check` passes.
- `./detector`, `./models`, and `./server` tests pass using a temporary module file and locally cached compatible transitive dependencies. No replacement is present in checked-in `go.mod`.
- An offline `go mod tidy` could not resolve uncached transitive module versions; no downloads were requested.
