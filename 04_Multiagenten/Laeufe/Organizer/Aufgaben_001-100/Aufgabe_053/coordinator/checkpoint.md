Task: Ensure oval.major("") returns "" while preserving non-empty behavior and API.
Changed oval/util.go with an early return for exactly empty input. Extended existing Test_major in oval/util_test.go with empty case.
Validation: GOPROXY=off GOSUMDB=off go test ./oval passed; git diff --check passed. No delegation used.
