Added Ubuntu 20.04 extended support through 1 April 2030 and Ubuntu 22.04 standard and extended support dates through 1 April 2027 and 1 April 2032 in [config/os.go](/app/config/os.go:137). Added tests confirming both releases are recognized and their support is active in 2026.

Verification passed: `go test ./config` and `git diff --check`.