VERDICT: ACCEPT

The patch in [detector/wordpress.go](/app/detector/wordpress.go) maps the requested WPScan fields, selects the requested core version, and leaves absent optional metadata empty. I found no correctness or regression issue. No correction is needed.

Tests passed:

- `GOPROXY=off GOSUMDB=off go test -mod=readonly ./detector -run 'Test(ConvertToVinfos|DetectWordPress|RemoveInactive)' -count=1`
- `GOPROXY=off GOSUMDB=off go test -mod=readonly ./detector -count=1`

TEST_ENVIRONMENT_PROBLEM: none.