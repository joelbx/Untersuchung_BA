Changed [srv.go](/app/lib/reversetunnel/srv.go:93) to store one `*localSite`, route service connections through it after validating the certificate cluster, and use it directly for site lookups, reconnect advisories, tunnel-close handling, and proxy fan-out.

Updated [localsite.go](/app/lib/reversetunnel/localsite.go:46) so `newlocalSite` derives its dependencies from the server and reuses `LocalAccessPoint` instead of creating another cached access point.

Verification: `go test ./lib/reversetunnel` passed, and `git diff --check` passed.