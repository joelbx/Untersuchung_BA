The config loader now reads `db.max_idle_conn`, `db.max_open_conn`, `db.conn_max_lifetime`, and `meta.check_for_updates`. Missing keys retain `Default()` values; update checks now default to `false` as required. The default and deprecated fixtures still load field-for-field equal to `Default()`.

Tests passed: `go test ./config ./cmd/flipt ./storage/db`. No delegation was used.