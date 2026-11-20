Task: Fix config loading for database pool options and update-check flag.
Status: Complete. Added database pool fields and config key loading, made update checks default to false, and isolated each Viper load. Extended fixture tests for configured values and omitted keys. `GOPROXY=off GOSUMDB=off go test ./...` passed; `git diff --check` passed.
