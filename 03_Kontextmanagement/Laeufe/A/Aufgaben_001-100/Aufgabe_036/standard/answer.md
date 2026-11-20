Updated the config loader to read the three database pool options and `meta.check_for_updates`. Update checks now default to `false` when the key is absent, while omitted pool options retain their defaults. The config fixtures and tests cover explicit values and field-by-field equality with `Default()`.

Verification: `go test ./config` and `git diff --check` passed.