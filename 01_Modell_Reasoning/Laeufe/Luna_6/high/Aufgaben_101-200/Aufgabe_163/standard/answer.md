Implemented database configuration using either a URL or separate protocol, host, port, user, password, name, and SQLite path fields. URL settings take precedence; key/value settings receive validation and engine-specific port defaults.

Normal connections and migrations now use the same internally generated target. Pool settings apply to migrations, and URL-related errors avoid exposing credentials. TLS certificate errors now identify the qualified setting.

Verification passed: `go test ./config ./storage/db ./cmd/flipt` and `git diff --check`.