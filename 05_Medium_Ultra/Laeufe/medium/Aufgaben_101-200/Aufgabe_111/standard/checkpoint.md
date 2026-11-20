# Checkpoint

Task: Support Amazon Linux 2023, 2025, 2027 and 2029 release normalization and EOL lookup.
Completed: Updated config/os.go version normalization and EOL dates; extended scanner /etc/system-release recognition; added ALAS2023 source links; added config tests for release and support boundaries.
Verified: git diff --check; GOPROXY=off GOSUMDB=off go test ./config ./scanner ./oval; focused config tests with -count=1.
Constraints honored: Local repository and tests only. No git history, index, or harness changes.
