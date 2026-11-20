Added a first-class `KEVs` field to vulnerabilities, with CISA and VulnCheck details, due-date normalization, a KEV CVE summary, and stable JSON ordering. Updated go-kev to a locally cached version that supports VulnCheck and added focused tests.

`GOPROXY=off GOSUMDB=off go test ./models ./detector` passed; `git diff --check` passed. No delegation was used.