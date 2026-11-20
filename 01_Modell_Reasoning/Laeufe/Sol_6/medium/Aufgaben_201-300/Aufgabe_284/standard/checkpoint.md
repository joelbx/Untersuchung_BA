# Checkpoint

Task complete: reversetunnel server now owns one local site and reuses the existing proxy access point. The local site constructor derives its auth client, access point, and peer client from the server. Local connection registration validates the certificate cluster and uses the single site. Site lookup, reconnect advisories, tunnel close handling, and proxy fan-out use that instance directly.

Verification: `go test ./lib/reversetunnel -count=1` passed; `git diff --check` passed.
