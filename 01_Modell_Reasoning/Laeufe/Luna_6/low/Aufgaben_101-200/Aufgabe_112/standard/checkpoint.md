# Fortinet CVE enrichment checkpoint

- Inspect existing CVE detection, content conversion, HTTP handler, and dependency versions.
- Add Fortinet detection and metadata enrichment across models and display selection.
- Run existing relevant Go tests and report outcomes.

## Progress

- Implemented Fortinet CPE eligibility, advisory conversion and aggregation, confidence ranking, advisory IDs, content type, display precedence, and both enrichment call sites.
- Updated go-cve-dictionary to the locally available prerelease that defines Fortinet models and detection methods.
- Relevant Go tests could not start because the offline module cache lacks `github.com/pelletier/go-toml/v2@v2.0.8` (`GOPROXY=off`). No downloads were attempted.
- Added internal Fortinet confidence values with the same score/order behavior as the corresponding NVD confidence levels, so all three Fortinet detection methods are representable in scan results.
