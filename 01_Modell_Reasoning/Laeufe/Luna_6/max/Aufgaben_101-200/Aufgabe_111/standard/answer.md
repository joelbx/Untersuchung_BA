Implemented Amazon Linux support across version detection, EOL handling, and OVAL lookup.

- [config/os.go](/app/config/os.go) recognizes releases 1, 2, 2022, 2023, 2025, 2027, and 2029; `YYYY.MM` maps to 1, and unrecognized versions map to `unknown`.
- Added standard support end dates: 2023 → June 30, 2028; 2025 → June 30, 2030; 2027 → June 30, 2032; 2029 → June 30, 2034. Unknown releases return `found=false`.
- [scanner/redhatbase.go](/app/scanner/redhatbase.go) parses Amazon Linux 2023 system release strings. [oval/util.go](/app/oval/util.go) selects the matching release data, and [oval/redhat.go](/app/oval/redhat.go) formats ALAS2023 advisory links.

Added regression tests for release parsing, OVAL selection, EOL dates, and support boundaries. `go test ./config ./scanner ./oval` passed.