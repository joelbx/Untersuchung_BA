Task: Fortinet advisory CVE detection and enrichment.
Status: Implemented and verified locally.
Changes: Upgraded go-cve-dictionary to cached Fortinet-capable version; added Fortinet content conversion, confidence ranking, CPE inclusion, advisory IDs, enrichment in scan/server, and report ordering/source links. Added focused tests.
Tests: GOPROXY=off GOSUMDB=off go test ./models ./detector ./server (passed); git diff --check (passed).
Delegation: none.
