# Checkpoint

Task: resolve the redundant local-site slice and duplicate cache construction in `reversetunnel.Server`.

Complete: `server` now owns one `*localSite`; startup creates it once via `newlocalSite(server)`. The site derives the local auth client, proxy access point, cluster name, auth addresses, and peer client from the server and shares the existing local access point. Service registration validates the certificate cluster and uses that singleton. Drain advisories, site lookups, close handling, and proxy fan-out use the singleton directly.

Validation: `go test ./lib/reversetunnel` passed. `git diff --check` passed.
