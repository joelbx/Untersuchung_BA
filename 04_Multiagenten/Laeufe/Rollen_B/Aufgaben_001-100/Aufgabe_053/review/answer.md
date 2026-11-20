VERDICT: FIX

The `major("")` change in [oval/util.go](/app/oval/util.go:280) meets the empty-input requirement and leaves the non-empty parsing path unchanged. The patch does not provide the three public functions listed under INTERFACES: `DetectPkgCves`, `DetectGitHubCves`, and `DetectWordPressCves` are absent from [report/report.go](/app/report/report.go). Add them with the specified signatures to satisfy that part of the stated contract.

**Tests:** `GOPROXY=off GOSUMDB=off go test ./oval -run '^Test_major$' -count=1`, `go test ./oval -count=1`, and `go test ./report -count=1` all passed with the same environment settings. `git diff --check` passed. **TEST_ENVIRONMENT_PROBLEM:** none.