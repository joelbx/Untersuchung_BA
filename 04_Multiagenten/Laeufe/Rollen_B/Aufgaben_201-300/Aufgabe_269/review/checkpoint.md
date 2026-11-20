VERDICT: FIX
CODE DEFECT: contrib/trivy/pkg/converter.go:72-103 and detector/library.go:293-321 accept any source and create trivy:<source> contents. models/cvecontents.go:341 limits GetCveContentTypes("trivy") to seven names. models/vulninfos.go:420,468,515,540 and tui/tui.go:948 iterate that fixed list, so a source such as trivy:alpine retains data in CveContents but its title/summary, CVSS scores, severity, and references are absent from those aggregated displays. Correction: aggregate source keys actually present in CveContents (with deterministic ordering), including TUI references; keep constants for commonly known sources.
TESTS: GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./contrib/trivy/pkg ./contrib/trivy/parser/v2 ./detector ./models ./tui -> exit 0. pkg, parser/v2, detector, models passed; tui reported [no test files].
TEST_ENVIRONMENT_PROBLEM: none.
No project code or tests changed during this review.
