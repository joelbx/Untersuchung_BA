VERDICT: FIX
Review complete. CODE_DEFECTS:
1. report/util.go:540-547 merges package data from current and previous scans into a single map keyed by package name. If a newly detected and a resolved CVE affect the same package, one scan version overwrites the other depending on map iteration order; each CVE cannot reliably show its required source package. Correct by preserving per-CVE/per-status package snapshots or equivalent, then render from that source.
2. report/slack.go:209, report/telegram.go:35-37, report/chatwork.go:36-41, and report/syslog.go:61 still render CVE IDs without status. Diff output through these writers cannot distinguish new and resolved vulnerabilities. Render the status in display text or a dedicated field while keeping CVE URL IDs clean.
TESTS: GOPROXY=off GOSUMDB=off go test ./models ./report ./subcmds => exit 0; models and report passed; subcmds has no test files. sqlite3 C compiler warning only. No TEST_ENVIRONMENT_PROBLEM.
