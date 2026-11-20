Updated `reversetunnel.Server` to keep one `localSite` and use it for connection registration, reconnect advisories, site lookup, cleanup, and proxy fan-out. The local site now reuses the server’s proxy access point instead of creating a second resource cache. Added tests for dependency reuse and cluster validation.

Verification: `go test ./lib/reversetunnel` passed; `git diff --check` passed.