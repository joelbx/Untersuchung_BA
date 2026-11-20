# Checkpoint

Task: Add Fortinet advisories to CVE detection, enrichment, and report model.
Status: inspecting local repository. `rg` is unavailable; using `find` and `grep`.
Verification: pending.

Implementation: Fortinet source included in CPE detection, enrichment, confidence, advisory IDs, content type, and display order. Dependency changed to locally cached go-cve-dictionary v0.9.1-0.20230925070138-66e5573a03bd.

Verification attempt: `GOPROXY=off GOSUMDB=off go test -mod=mod ./detector ./models ./server` exited 1: `go: github.com/pelletier/go-toml/v2@v2.0.8: module lookup disabled by GOPROXY=off`. The newer dictionary requests an uncached indirect version, so compilation and tests remain unverified with this command. No dependencies downloaded.

Additional offline verification attempt: `cp go.mod /tmp/vuls-fortinet-test.mod && cp go.sum /tmp/vuls-fortinet-test.sum && go mod edit -modfile=/tmp/vuls-fortinet-test.mod -require=github.com/pelletier/go-toml/v2@v2.1.0 && GOPROXY=off GOSUMDB=off go test -mod=mod -modfile=/tmp/vuls-fortinet-test.mod ./detector ./models ./server` exited 1: `go: gorm.io/gorm@v1.25.2: module lookup disabled by GOPROXY=off`.
Follow-up temporary override: `go mod edit -modfile=/tmp/vuls-fortinet-test.mod -require=gorm.io/gorm@v1.25.4 && GOPROXY=off GOSUMDB=off go test -mod=mod -modfile=/tmp/vuls-fortinet-test.mod ./detector ./models ./server` exited 1: `go: modernc.org/sqlite@v1.23.1: module lookup disabled by GOPROXY=off`.
Final required test attempt: `GOPROXY=off GOSUMDB=off go test -mod=mod ./detector ./models ./server` exited 1: `go: github.com/pelletier/go-toml/v2@v2.0.8: module lookup disabled by GOPROXY=off`.
Uncertainty: detector, models, and server tests could not compile or execute because required transitive versions are absent from the local module cache. Dependency downloads prohibited.
