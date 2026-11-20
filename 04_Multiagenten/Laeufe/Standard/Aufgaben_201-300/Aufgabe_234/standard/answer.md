SQLite access now uses one `*sql.DB` with the requested connection options. Persistence transactions use the connection passed to `New()`, and scrobble play-count writes use the transaction object.

The issue’s read/write builder instructions conflict with its stated goal of removing that split, so I followed the unified-connection requirements.

Tests passed: `go test ./db ./persistence ./core/scrobbler`.