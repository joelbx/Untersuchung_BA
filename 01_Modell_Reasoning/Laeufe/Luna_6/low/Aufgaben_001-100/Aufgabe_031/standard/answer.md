Updated `config.Load` to skip `ReadInConfig` when the path is empty, allowing defaults and environment overrides to be applied. Added coverage for both requested variables, default values, and env precedence over file values.

`go test ./internal/config` and `git diff --check` passed.