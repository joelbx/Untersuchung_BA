# Checkpoint

Implemented Fortinet CVE detection and enrichment:

- Upgraded `go-cve-dictionary` to the locally cached version that defines Fortinet advisory models and detection methods.
- Included Fortinet-only entries in CPE results, converted advisory metadata to `CveContent`, and included Fortinet advisory IDs and confidence signals.
- Routed scan and HTTP server enrichment through `FillCvesWithNvdJvnFortinet`.
- Added Fortinet content type and display precedence for titles, summaries, and CVSS v3.

Validation: `gofmt` and `git diff --check` pass. Relevant Go tests were attempted with `GOPROXY=off`; dependency graph resolution stopped before compilation because `github.com/pelletier/go-toml/v2@v2.0.8` is not present in the local module cache. External downloads are unavailable for this task.
