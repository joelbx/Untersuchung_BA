Updated [config.go](/app/config/config.go) to load the three database pool options and `meta.check_for_updates`. When the update-check key is absent, the value is now false; omitted pool options retain their defaults.

Extended the [config tests](/app/config/config_test.go) and fixtures to cover explicit values and default preservation. `go test ./config ./cmd/flipt` passed.