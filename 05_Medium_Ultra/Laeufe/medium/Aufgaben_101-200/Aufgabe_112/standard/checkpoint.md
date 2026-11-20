# Checkpoint

Task: Integrate Fortinet advisories into CVE detection, enrichment, and report selection.
Status: Complete.
Changes: Upgraded go-cve-dictionary from cached modules; added Fortinet CVE conversion, confidence ranking, advisory IDs, source filtering, enrichment, and report ordering. Added focused confidence, conversion, and report priority tests.
Verification: GOPROXY=off GOSUMDB=off go test -mod=readonly ./detector ./models ./server passed; git diff --check passed.
Constraints: Used local repository and cached modules only; preserved git history, index baseline, and harness configuration.
