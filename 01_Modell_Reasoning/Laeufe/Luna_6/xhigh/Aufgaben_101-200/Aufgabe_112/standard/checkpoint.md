# Fortinet CVE integration checkpoint

- Repository: `/app`
- Task: include Fortinet advisories in CVE detection, enrichment, confidence, and content selection.
- Implemented: upgraded `go-cve-dictionary` and its required module versions; CPE lookup retains NVD or Fortinet results; added Fortinet conversion/enrichment, advisory IDs, and confidence mapping; added Fortinet to content selection and refresh comparisons; updated the main detector and HTTP handler.
- Validation: `gofmt` and `git diff --check` pass. Focused tests (`go test ./models ./detector ./server`) were attempted with `GOPROXY=off`; they could not start because required module versions are missing from the local cache (first missing: `github.com/pelletier/go-toml/v2@v2.0.8`). No dependency downloads were made.
- Work is implemented; final response should note the offline test limitation.
