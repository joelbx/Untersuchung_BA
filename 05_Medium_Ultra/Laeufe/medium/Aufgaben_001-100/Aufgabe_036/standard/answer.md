Updated [config.go](/app/config/config.go) so `Load` reads the three DB pool options and `meta.check_for_updates`. An absent update-check key now defaults to `false`, while absent keys leave the other defaults intact. Expanded the config tests to cover explicit values and field-for-field equality with `Default()`.

`go test ./...` and `git diff --check` passed.