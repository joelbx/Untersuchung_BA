VERDICT: FIX

The applied patch has two code defects:

- [report/util.go](/app/report/util.go:540) stores current and previous package versions in one map keyed by package name. If a new CVE and a resolved CVE affect the same package, one version overwrites the other. Preserve package data for each CVE’s scan source.
- [Slack](/app/report/slack.go:209), [Telegram](/app/report/telegram.go:35), [Chatwork](/app/report/chatwork.go:36), and [Syslog](/app/report/syslog.go:61) output CVEs without their diff status. Include `+` or `-` in those reports.

Tests: `GOPROXY=off GOSUMDB=off go test ./models ./report ./subcmds` exited 0. `models` and `report` passed; `subcmds` has no test files. No TEST_ENVIRONMENT_PROBLEM.