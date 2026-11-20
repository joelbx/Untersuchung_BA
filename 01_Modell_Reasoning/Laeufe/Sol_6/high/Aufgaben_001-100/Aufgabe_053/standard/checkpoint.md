Task: Ensure oval.major("") returns "" while preserving existing non-empty behavior and API.
Status: Added an exact empty-input guard in oval/util.go and a regression case in oval/util_test.go. Existing parsing path for non-empty input is unchanged.
Validation: GOPROXY=off GOSUMDB=off go test ./oval passed; git diff --check passed.
