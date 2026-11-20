Task: Make oval.major("") return "" while preserving non-empty behavior and API.
Status: Complete.
Changes: Added an empty-input guard in oval/util.go and a regression case in oval/util_test.go.
Verification: GOPROXY=off GOSUMDB=off go test ./oval -run '^Test_major$' -count=1; GOPROXY=off GOSUMDB=off go test ./oval -count=1; git diff --check. All passed.
