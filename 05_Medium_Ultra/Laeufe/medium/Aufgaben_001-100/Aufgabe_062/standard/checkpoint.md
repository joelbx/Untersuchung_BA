Task: Fix ContextReader terminal restoration for canceled/closed password reads and NotifyExit.
Status: Implemented and verified locally.
Changes: Restore terminal on canceled password reads, clean-read transition, close-time restoration and error propagation; add NotifyExit for global stdin and call it after tsh Run; add focused regression tests.
Verification: GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./lib/utils/prompt -count=1 passed; git diff --check passed. A broader tool/tsh test invocation was stopped during lengthy dependency compilation after the prompt package had passed.
