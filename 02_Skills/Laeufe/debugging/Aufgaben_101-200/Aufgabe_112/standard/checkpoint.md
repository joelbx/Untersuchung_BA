# Fortinet CVE integration checkpoint

Investigation started. Trace detection, enrichment, model conversion, ordering, and dependency compatibility before edits. Record reproduction and test results here.

Root cause: `detectCveByCpeURI` excludes every non-NVD detail when JVN is disabled; both CLI and HTTP call `FillCvesWithNvdJvn`, which converts only NVD/JVN; `getMaxConfidence` checks only NVD/JVN. The old dictionary dependency (v0.8.4) has no Fortinet model. Cached v0.9.1-0.20230925070138-66e5573a03bd supplies `Fortinets`, `HasFortinet`, and Fortinet detection method constants. Working NVD/JVN conversion and source ordering are the reference patterns.

Reproduction: added Fortinet confidence cases to `Test_getMaxConfidence`. `GOPROXY=off GOSUMDB=off go test -mod=mod ./detector -run Test_getMaxConfidence -count=1` failed as expected: Fortinet exact returned NVD rough (80), and Fortinet-only rough/vendor returned empty confidence. Initial runs were blocked by cached-module version gaps: go-toml/v2 v2.0.8, gorm v1.25.2, sqlite v1.23.1, and memory v1.6.0; pinned available versions in go.mod and retried. No dependencies were downloaded.

Implementation: upgraded go-cve-dictionary to cached Fortinet-capable revision; included Fortinet-only CPE details; converted advisory metadata and attached multiple advisories; evaluated Fortinet confidence; added Fortinet content type and report ordering; wired CLI and HTTP enrichment. Added conversion and HTTP-backed detection/enrichment tests.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod ./detector ./models ./server` passed after implementation. First `GOPROXY=off GOSUMDB=off go test -mod=mod ./...` failed because the initial summary order moved RedHat after NVD; adjusted order to preserve family priority while placing Fortinet before NVD. Reran the same full command; it passed. `git diff --check` passed.

Final verification after showing Fortinet advisory titles in `Titles`: `GOPROXY=off GOSUMDB=off go test -mod=mod ./...` passed (exit 0).
