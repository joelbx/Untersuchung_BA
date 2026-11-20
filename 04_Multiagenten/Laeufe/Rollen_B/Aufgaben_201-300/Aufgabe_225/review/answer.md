VERDICT: FIX

The patch populates `KEVs` in [detector/kevuln.go](/app/detector/kevuln.go:82), but existing report and TUI paths still read `AlertDict.CISA` in [models/scanresults.go](/app/models/scanresults.go:271), [reporter/util.go](/app/reporter/util.go:568), and [tui/tui.go](/app/tui/tui.go:815). Newly fetched KEVs therefore disappear from those summaries and displays. Update those readers to use `KEVs` while retaining support for CISA alerts in older JSON.

Tests: `GOPROXY=off GOSUMDB=off go test ./models ./detector` passed for both packages. No `TEST_ENVIRONMENT_PROBLEM`. This was an independent review; I made no project code changes.