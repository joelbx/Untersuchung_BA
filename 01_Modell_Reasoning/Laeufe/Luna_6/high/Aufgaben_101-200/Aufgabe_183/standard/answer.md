Implemented the Ubuntu lifecycle updates in [config/os.go](/app/config/os.go) and added Ubuntu 22.04 to the CVE lookup allowlist in [gost/ubuntu.go](/app/gost/ubuntu.go). Added regression coverage for the lifecycle dates and release recognition.

Verification passed: `go test ./config ./gost` and `git diff --check`.