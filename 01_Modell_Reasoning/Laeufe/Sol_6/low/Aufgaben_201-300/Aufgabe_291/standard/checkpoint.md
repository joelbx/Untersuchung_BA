Task: Add NVD CVSS v4.0 conversion and aggregation.
Status: Complete. Existing CveContent CVSS v4.0 fields retained. Updated cached go-cve-dictionary dependency for Nvd.Cvss40, mapped NVD metrics by Source, and added Nvd after Mitre in score aggregation. Added focused tests.
Verification: GOPROXY=off GOSUMDB=off go test -mod=mod ./models -count=1 passed.
