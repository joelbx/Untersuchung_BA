Implemented OS EOL lookup and warnings in [config/os.go](/app/config/os.go). Scan results now evaluate EOL status at the scan timestamp, and summaries render warnings as `Warning: <message>`. Amazon Linux release variants are normalized for lookup.

Centralized major version parsing in [version/version.go](/app/version/version.go), exposed through `util.Major`, and replaced the duplicated parsers.

Verification passed: `go test ./...` and `go test ./report`. `git diff --check` passed.