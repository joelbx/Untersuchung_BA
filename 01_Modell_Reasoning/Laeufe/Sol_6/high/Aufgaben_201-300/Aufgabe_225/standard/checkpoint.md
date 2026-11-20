# Checkpoint

Completed: added first-class KEV model and `VulnInfo.KEVs`; mapped CISA and VulnCheck data from database and HTTP, including XDB and reported exploitation details; normalized invalid due dates; added KEV CVE summary and stable JSON ordering. Upgraded `go-kev` to the locally cached version that supports both sources. Retained `AlertDict.CISA` for legacy JSON.

Validation passed: `git diff --check`; `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test -mod=mod ./models ./detector`.
