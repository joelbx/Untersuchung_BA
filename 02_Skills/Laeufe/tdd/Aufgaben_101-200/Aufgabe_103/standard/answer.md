Updated the RPM parsers to preserve empty release fields, build source versions without a trailing hyphen, parse the supported `-src.rpm` filenames, reject malformed names, and handle update listings with epochs. Added regression tests.

Verification passed: `go test ./scanner -count=1`, offline `go test ./...`, and `git diff --check`.