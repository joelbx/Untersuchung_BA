Fixed the external scanner’s XML parsing in [scanner/portscan.go](/app/scanner/portscan.go): it now parses stdout separately from stderr and includes stderr in command errors. Added regression coverage for both cases.

Both test commands flagged by the reviewer passed: `go test ./config ./scanner` and `go test ./subcmds ./models`, with `GOPROXY=off GOSUMDB=off`.

**TEST_ENVIRONMENT_PROBLEM:** `nmap` is not installed locally, so a live scan could not be verified.