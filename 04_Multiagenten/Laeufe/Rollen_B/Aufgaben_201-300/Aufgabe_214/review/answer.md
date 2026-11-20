VERDICT: FIX

**Code defect:** [scanner/portscan.go](/app/scanner/portscan.go:84) uses `CombinedOutput()` and passes the result to the XML parser. If nmap writes a warning to stderr alongside valid XML on stdout, the scan fails to parse. Capture stdout and stderr separately; parse stdout and include stderr in command errors.

**TEST_ENVIRONMENT_PROBLEM:** `nmap` is not installed locally, so a live nmap scan could not be verified.

Existing local tests executed:

- `GOPROXY=off GOSUMDB=off go test ./config ./scanner` — passed.
- `GOPROXY=off GOSUMDB=off go test ./subcmds ./models` — passed; `subcmds` has no test files.