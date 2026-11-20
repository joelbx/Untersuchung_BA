# Checkpoint

Task: Ensure `oval.major("")` returns `""` while preserving behavior for non-empty inputs and keeping the existing signature. Provide the three report API signatures listed in the request.

Implementation: Added an exact empty-input guard and regression case. Added `DetectPkgCves`, `DetectGitHubCves`, and `DetectWordPressCves` in `report/report.go`, reusing existing detection logic.

Verification: `GOPROXY=off go test ./oval ./report` passed. `git diff --check` passed. No dependency downloads were enabled.
