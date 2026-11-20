Added `VulnInfo.KEVs` with CISA and VulnCheck details, mapped both sources into it, normalized placeholder due dates, and added KEV summary and JSON ordering. The VulnCheck-capable `go-kev` version was available locally; no dependencies were downloaded.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=readonly ./models ./detector` passed.