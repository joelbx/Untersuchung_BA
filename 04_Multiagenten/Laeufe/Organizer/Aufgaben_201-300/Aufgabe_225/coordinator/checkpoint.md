Task: Add first-class KEV entries to VulnInfo, with CISA/VulnCheck source data, summary, and stable JSON ordering.
Status: Complete. Implemented model and converter; updated go-kev to locally cached version supporting VulnCheck; added focused tests. GOPROXY=off GOSUMDB=off go test ./models ./detector passed. git diff --check passed.
Delegation: none.
Constraints: local code/tests only; no downloads; preserved git history, index baseline and harness config.
