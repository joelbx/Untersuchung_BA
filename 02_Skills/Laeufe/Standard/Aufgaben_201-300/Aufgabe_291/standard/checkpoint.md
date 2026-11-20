# Checkpoint

Task: add NVD CVSS v4.0 conversion and aggregation.

Completed:
- Confirmed CveContent already has Cvss40Score, Cvss40Vector, and Cvss40Severity.
- Updated go-cve-dictionary to the locally cached version containing Nvd.Cvss40 and added its checksums.
- ConvertNvdToModel now associates v4.0 metrics by Source and persists all three fields.
- Cvss40Scores now emits MITRE then NVD entries.
- Added tests for source association, v3 coexistence, and aggregation order.

Checks passed:
- GOPROXY=off GOSUMDB=off go test -mod=mod ./models -run 'TestConvertNvdToModelCvss40Sources|TestCvss40ScoresMitreThenNvd|TestVulnInfo_Cvss40Scores' -count=1
- GOPROXY=off GOSUMDB=off go test -mod=mod ./models -count=1
- git diff --check
