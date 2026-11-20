Implemented Fortinet advisory support across CVE detection and reporting:

- Fortinet-only CVEs are retained during CPE detection, with advisory IDs and confidence signals included.
- Fortinet advisories are converted into `CveContent` with title, summary, CVSS v3, URL, CWE IDs, references, and timestamps.
- Scan and HTTP server enrichment use `FillCvesWithNvdJvnFortinet`.
- Added the Fortinet content type and the requested display ordering.
- Updated `go-cve-dictionary` to a version with Fortinet models and detection methods.

`gofmt` and `git diff --check` pass. I attempted the relevant tests offline, but dependency resolution stopped before compilation because `go-toml/v2 v2.0.8` is missing from the local cache. The checkpoint is recorded in `.codex-role-output/checkpoint.md`.