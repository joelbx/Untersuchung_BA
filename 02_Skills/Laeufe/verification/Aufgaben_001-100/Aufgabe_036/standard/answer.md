Updated [config/config.go](/app/config/config.go) so `Load` reads the three database pool options and `meta.check_for_updates`. The update-check default is now `false` when the key is absent. Tests cover explicit values and confirm that the default and deprecated fixtures load field-for-field as `Default()`.

Verification: `go test ./...` passed.