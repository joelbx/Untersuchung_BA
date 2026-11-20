VERDICT: FIX

The relevant tests passed, but I found two code defects:

- [source.go](/app/internal/storage/fs/oci/source.go:81): `Subscribe` compares digest values across separate lock scopes. A concurrent `Get` can cause it to miss an update or send an older snapshot. Track the last delivered digest and capture the snapshot and digest together for each poll.
- [file.go](/app/internal/oci/file.go:50): Remote store construction ignores the configured authentication and insecure transport settings. Apply those settings so configured registries can be fetched.

Tests executed successfully: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/oci ./internal/storage/fs/oci ./internal/storage/fs/...` and `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config ./internal/cmd`. TEST_ENVIRONMENT_PROBLEM: none.