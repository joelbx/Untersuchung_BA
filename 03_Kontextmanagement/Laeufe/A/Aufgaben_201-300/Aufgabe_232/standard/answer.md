Implemented OS lifecycle lookup and scan warnings in [config/os.go](/app/config/os.go) and [scan/eol.go](/app/scan/eol.go). Scan summaries now show each warning with the required `Warning: ` prefix, in evaluation order. Major version parsing is shared across components.

The affected package tests passed: `go test ./config ./scan ./report ./util ./oval ./gost`.