Updated [config.go](/app/config/config.go) so `Load` reads the database pool options and `meta.check_for_updates`. Update checks now default to `false`, and each load uses fresh Viper state so omitted keys retain `Default()` values. Added fixture coverage for configured values and for loading `default.yml` and `deprecated.yml` after other files.

`go test ./...` and `git diff --check` passed.