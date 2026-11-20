Task: Add NVD CVSS v4.0 conversion and aggregation in Mitre/Nvd order.
Status: Complete.
Findings: CveContent already had Cvss40Score, Cvss40Vector, Cvss40Severity. Pinned go-cve-dictionary lacked Nvd.Cvss40; upgraded to newer version already in local module cache.
Changes: NVD v4 metrics grouped by Source and copied into CveContent; v4 aggregation includes Mitre then Nvd; tests cover conversion, source association, and ordering.
Verification: GOPROXY=off GOSUMDB=off go test ./models -count=1 passed; GOPROXY=off GOSUMDB=off go test ./reporter/... -run '^$' passed; git diff --check passed.
Delegation: none.
