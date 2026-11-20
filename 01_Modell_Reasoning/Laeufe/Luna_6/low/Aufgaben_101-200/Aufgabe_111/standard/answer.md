Implemented Amazon Linux release normalization and EOL mappings in [config/os.go](/app/config/os.go). Added regression tests for supported and unknown releases, plus the Amazon Linux 2023 support boundary in [config/os_test.go](/app/config/os_test.go).

Verification passed: `go test ./config` and `git diff --check`.