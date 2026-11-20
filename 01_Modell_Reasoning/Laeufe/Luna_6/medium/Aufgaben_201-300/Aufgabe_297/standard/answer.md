Implemented reverse proxy authentication, UI session initialization, and recursive log redaction.

The configured whitelist controls whether the configured username header is trusted. Successful authentication creates missing users (making the first user admin), updates last login, and includes a token and Subsonic credentials in the frontend config. Untrusted or unsuccessful requests receive no `auth` field.

Verification: `go test ./server/app ./log ./conf` and `git diff --check` pass.