Implemented Fortinet advisory support across detection, enrichment, and reporting. CPE matching now includes Fortinet-only CVEs, confidence considers Fortinet alongside NVD and JVN, and Fortinet advisory IDs and metadata are added to results. The detector pipeline and HTTP handler use the new enrichment function. I also updated content ordering, refresh comparisons, and the `go-cve-dictionary` dependency.

`gofmt` and `git diff --check` pass. The focused tests could not start: `GOPROXY=off go test ./models ./detector ./server` is blocked because the local module cache lacks `github.com/pelletier/go-toml/v2@v2.0.8`. No downloads were made.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)