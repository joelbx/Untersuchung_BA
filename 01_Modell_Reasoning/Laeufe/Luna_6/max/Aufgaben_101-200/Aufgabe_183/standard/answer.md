Implemented the Ubuntu lifecycle and release support updates:

- Added Ubuntu 20.04 extended support through 2030-04-01 and Ubuntu 22.04 support dates through 2027-04-01 standard and 2032-04-01 extended in [config/os.go](/app/config/os.go:137).
- Enabled Ubuntu 22.04 in the GOST release allowlist and OVAL processing in [gost/ubuntu.go](/app/gost/ubuntu.go:23) and [oval/debian.go](/app/oval/debian.go:398).
- Added regression coverage for lifecycle windows and GOST recognition.

Validation passed: `go test ./config ./gost ./oval` and `git diff --check`.