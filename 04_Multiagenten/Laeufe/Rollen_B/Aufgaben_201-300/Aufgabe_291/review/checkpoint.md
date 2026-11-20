VERDICT: ACCEPT
Reviewed the existing patch. CveContent already contains Cvss40Score, Cvss40Vector, and Cvss40Severity in models/cvecontents.go. The patch reads nvd.Cvss40 by Source, persists the fields in NVD CveContent, and aggregates v4 scores in Mitre, Nvd order. No correctness defect found.
Tests executed successfully:
- GOPROXY=off GOSUMDB=off go test ./models -run 'TestConvertNvdToModelCvss40|TestVulnInfo_Cvss40Scores|TestVulnInfo_MaxCvss40Score' -count=1 (exit 0)
- GOPROXY=off GOSUMDB=off go test ./models -count=1 (exit 0)
- git diff --check (exit 0)
No project code or tests changed during review.
