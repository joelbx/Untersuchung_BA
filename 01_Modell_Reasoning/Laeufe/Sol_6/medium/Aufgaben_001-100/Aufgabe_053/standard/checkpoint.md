Task: ensure oval.major("") returns "" while preserving non-empty behavior.
Status: complete. Added an exact empty-input guard and a table test.
Verification: GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./oval -run '^Test_major$' -count=1; GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./oval -count=1; git diff --check. All passed.
