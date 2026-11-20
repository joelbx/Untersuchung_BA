# Checkpoint

Implemented dedicated `VulnInfo.KEVs`, source-specific KEV models, summary and sorting. Updated the cached go-kev dependency to the version that supports CISA and VulnCheck and mapped both sources in `FillWithKEVuln`. Added focused tests. `rg` is unavailable; used local grep/find.

Validation passed: `GOPROXY=off GOSUMDB=off go test -mod=mod ./models ./detector`; focused `TestKEVSummaryAndJSONSort` and `TestConvertKEVulns` also passed. `git diff --check` passed.
