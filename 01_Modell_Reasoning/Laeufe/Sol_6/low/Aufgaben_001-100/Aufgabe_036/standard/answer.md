Updated the config loader to read the three database pool options and `meta.check_for_updates`. An absent update-check key now remains `false` in `Default()`, so the default and deprecated fixtures still load field-for-field as `Default()`.

Updated the config tests and fixture. `go test ./config` and `git diff --check` passed.