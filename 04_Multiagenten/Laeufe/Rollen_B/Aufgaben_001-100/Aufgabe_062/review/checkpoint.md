VERDICT: FIX
Code defect: lib/utils/prompt/context_reader.go:155-167 snapshots password mode before calling term.ReadPassword. A cancellation at :223-229 or Close at :300-305 can restore the terminal and return before that call begins. The worker then starts term.ReadPassword, which disables echo, leaving the shell locked until another line is entered. Synchronize the worker's password-mode entry with cancellation/Close and prevent password mode from starting after restoration. The current fakeTerm tests do not exercise this timing.
Tests executed: `GOTOOLCHAIN=local GOPROXY=off go test ./lib/utils/prompt` PASS; `GOTOOLCHAIN=local GOPROXY=off go test ./tool/tsh -run '^TestFailedLogin$' -count=1` PASS; `git diff --check` PASS.
TEST_ENVIRONMENT_PROBLEM: none.
No project code or tests changed during review.
