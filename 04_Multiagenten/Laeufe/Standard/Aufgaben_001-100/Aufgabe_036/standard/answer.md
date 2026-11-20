Updated the config loader to read the three database pool options and `meta.check_for_updates`. The update-check default is now `false`, so omitted keys retain `Default()` values; the default and deprecated fixtures still match it field for field. The advanced fixture tests explicit pool values and an enabled update flag.

`go test ./config`, `go test ./...`, and `git diff --check` passed.