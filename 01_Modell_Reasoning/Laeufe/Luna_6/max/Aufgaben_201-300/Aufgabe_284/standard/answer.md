Implemented the single `localSite` field and refactored connection registration, validation, lookups, reconnect advisories, close handling, and proxy fan-out to use it. `newlocalSite` now uses the server’s existing `LocalAccessPoint` and clients instead of creating another access point.

Updated the existing constructor test. Validation passed: `go test ./lib/reversetunnel`, `gofmt`, and `git diff --check`.

Changes: [srv.go](/app/lib/reversetunnel/srv.go:93), [localsite.go](/app/lib/reversetunnel/localsite.go:46), [localsite_test.go](/app/lib/reversetunnel/localsite_test.go:36).