Implemented first-class KEV support on `VulnInfo`, with CISA and VulnCheck metadata and feed conversion in [kev_mapping.go](/app/detector/kev_mapping.go:18) and [kevuln.go](/app/detector/kevuln.go:50). New detections populate `KEVs`; `AlertDict.CISA` remains available for older JSON.

Added KEV summary reporting and sorting by source and vulnerability name in [scanresults.go](/app/models/scanresults.go:255), plus the requested types in [kev.go](/app/models/kev.go:5). Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

Validation passed: `GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter`; `git diff --check` passed.