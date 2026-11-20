Updated the config loader to read database pool limits, connection lifetime, and `meta.check_for_updates`. When the update-check key is absent, it now defaults to `false`. Tests cover explicit values and confirm that the default fixtures load field-for-field as `Default()`.

`go test ./...` passed offline.