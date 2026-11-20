Updated library scanning and reporting so vulnerabilities retain their lockfile path. Each lockfile is analyzed separately, library lookup uses both path and name, and findings for the same CVE are merged across files. Trivy imports and TUI output now carry the path too.

The relevant tests passed: `go test ./models ./scan ./report ./libmanager ./contrib/trivy/parser`.