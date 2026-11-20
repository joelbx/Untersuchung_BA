# Checkpoint

Task: Add NVD CVSS v4.0 model conversion and aggregation support.

The existing CveContent already contains Cvss40Score, Cvss40Vector, and Cvss40Severity. Updated go-cve-dictionary to the newer version present in the local module cache, which defines Nvd.Cvss40. ConvertNvdToModel now groups v4.0 metrics by Source and writes them into CveContent. Cvss40Scores now reads Mitre, then Nvd. Added focused conversion and ordering tests.

Verification completed:
- `GOPROXY=off GOSUMDB=off go test ./models -run 'TestConvertNvdToModelCvss40|TestCvss40ScoresMitreThenNvd|TestVulnInfo_Cvss40Scores' -count=1`: passed.
- `GOPROXY=off GOSUMDB=off go test ./models -count=1`: passed.
- `GOPROXY=off GOSUMDB=off GOMAXPROCS=2 go test -p 2 ./detector -count=1`: passed.
- `git diff --check`: passed.

An earlier combined `GOPROXY=off GOSUMDB=off go test ./models ./detector -count=1` run was interrupted while compiling detector dependencies; the separate detector retry above completed successfully.
