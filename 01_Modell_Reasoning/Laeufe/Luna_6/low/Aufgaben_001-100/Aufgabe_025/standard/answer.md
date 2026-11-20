Implemented exact `${VARIABLE_NAME}` substitution as the first hook in `DecodeHooks`. Substituted values continue through later hooks, allowing conversions such as integer ports and log encodings. Added coverage for multiple variables, unset or invalid references, and partial matches.

`go test ./internal/config` passes. `go.work.sum` also shows as modified; I did not intentionally edit it.