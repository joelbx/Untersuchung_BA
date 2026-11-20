VERDICT: ACCEPT

The patch captures NVD CVSS v4.0 metrics by source and returns v4.0 scores in Mitre, Nvd order. The three requested `CveContent` fields were already present. I found no correctness defect.

Both relevant test commands passed:

- `GOPROXY=off GOSUMDB=off go test ./models -run 'TestConvertNvdToModelCvss40|TestVulnInfo_Cvss40Scores|TestVulnInfo_MaxCvss40Score' -count=1`
- `GOPROXY=off GOSUMDB=off go test ./models -count=1`

`git diff --check` also passed.