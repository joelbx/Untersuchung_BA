VERDICT: ACCEPT

Review complete. Fedora, SUSE, and macOS values match the issue; new Windows rollups use named fields, preserve prior entries, and have ascending revisions. No blocking defect found. FreeBSD 13/14 dates also changed outside the requested scope.

Tests executed locally with network disabled:
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./config -run 'TestEOL_IsStandardSupportEnded' -count=1` — PASS.
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_windows_(detectKBsFromKernelVersion|recentRollupsFromKernelVersion)$' -count=1` — PASS.
- `git diff --check` — PASS.
