VERDICT: FIX

**Code defect:** Both conversion paths create `trivy:<source>` entries for any source, but [GetCveContentTypes("trivy")](/app/models/cvecontents.go:338) lists only seven. The metadata methods in [vulninfos.go](/app/models/vulninfos.go:420) and references display in [tui.go](/app/tui/tui.go:948) iterate that fixed list. A source such as `trivy:alpine` therefore remains in `CveContents` but loses its severity, CVSS, summary, and references from those views. Aggregate the Trivy keys present in `CveContents` in a stable order.

**Tests:** `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./contrib/trivy/pkg ./contrib/trivy/parser/v2 ./detector ./models ./tui` exited 0. The first four packages passed; `tui` has no test files. `TEST_ENVIRONMENT_PROBLEM: none`.

I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md). I made no project code or test changes.