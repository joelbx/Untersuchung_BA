# Checkpoint

Resolved NVD CVSS v4.0 conversion and aggregation. `CveContent` already contained the three v4.0 fields. Updated the locally cached go-cve-dictionary version to one with `Nvd.Cvss40`, copied source-specific metrics into NVD content, and added NVD after MITRE in `Cvss40Scores`.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod ./models` passed; `GOPROXY=off GOSUMDB=off go test -mod=mod ./detector ./reporter/...` passed; `git diff --check` passed.
