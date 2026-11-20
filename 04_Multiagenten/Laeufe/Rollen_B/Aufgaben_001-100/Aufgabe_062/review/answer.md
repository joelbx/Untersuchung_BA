VERDICT: FIX

**Code defect:** [context_reader.go](/app/lib/utils/prompt/context_reader.go:155) can select password mode, then pause before calling `term.ReadPassword`. Meanwhile, cancellation or `Close` can restore the terminal and return. When the worker resumes, `ReadPassword` disables echo again, leaving the terminal locked. The worker must be prevented from entering password mode after restoration.

Relevant existing tests passed:

- `GOTOOLCHAIN=local GOPROXY=off go test ./lib/utils/prompt`
- `GOTOOLCHAIN=local GOPROXY=off go test ./tool/tsh -run '^TestFailedLogin$' -count=1`

**TEST_ENVIRONMENT_PROBLEM:** None. No project code or tests were changed during this review.