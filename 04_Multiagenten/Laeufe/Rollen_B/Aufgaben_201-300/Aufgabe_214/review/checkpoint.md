VERDICT: FIX
Code defect: scanner/portscan.go:84-89 merges nmap stderr with XML stdout via CombinedOutput; valid XML plus a warning on stderr fails xml.Unmarshal. Capture stdout and stderr separately, parse only stdout, include stderr on command failure.
Additional concern: privileged scans for non-root users validate file capabilities but invocation does not pass nmap --privileged or NMAP_PRIVILEGED.
Tests: GOPROXY=off GOSUMDB=off go test ./config ./scanner (pass); GOPROXY=off GOSUMDB=off go test ./subcmds ./models (pass; subcmds has no test files, sqlite3 compiler warning).
Environment: nmap is absent locally; live nmap execution unverified.
