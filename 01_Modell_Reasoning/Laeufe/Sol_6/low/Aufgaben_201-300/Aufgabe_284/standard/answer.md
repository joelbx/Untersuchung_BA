Updated `reversetunnel.Server` to keep one `localSite` and use it directly for connection registration, reconnect advice, site lookup, and proxy updates. The local site now reuses the server’s existing proxy access point and clients instead of creating a second resource cache. I also added a test for local cluster validation.

Verification: `go test ./lib/reversetunnel -count=1` passed.