# Checkpoint

Task: Amazon Linux 2023/2025/2027/2029 version recognition and EOL handling.
Status: implemented in `config/os.go`; added regression tests in `config/amazon_linux_test.go`.
TDD: focused tests failed before implementation because single-token versions mapped to 1, unknown versions mapped incorrectly, and new EOL entries were absent. The focused config suite then passed.
Verification: `GOPROXY=off GOSUMDB=off go test ./config -count=1` passed; `GOPROXY=off GOSUMDB=off go test ./...` passed; `git diff --check` passed.
Evidence limit: local repository did not contain an authoritative lifecycle source for future Amazon Linux releases. Dates use March 15 five years after each release year, consistent with the Amazon Linux 2023 lifecycle used by this patch. No live host or ALAS advisory service was available for integration verification.
