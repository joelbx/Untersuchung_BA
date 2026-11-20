Task: make oval.major("") return "" while preserving non-empty behavior and API.
Status: complete. Added exact empty-input guard and regression case.
Validation: GOPROXY=off go test ./oval -run '^Test_major$' -count=1; GOPROXY=off go test ./oval -count=1; GOPROXY=off go test ./report -run '^$'; git diff --check. All passed.
