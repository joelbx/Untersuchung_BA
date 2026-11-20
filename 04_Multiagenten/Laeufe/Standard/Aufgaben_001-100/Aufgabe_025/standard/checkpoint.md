Task: Add exact ${VAR} environment substitution to YAML configuration decoding before existing hooks.
Status: Complete. Added first decode hook, integrated tests for multiple variables, integer/duration/string values, ordinary Flipt overrides, exact matching, missing and empty variables, and named string values.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/config ./config -count=1 passed; git diff --check passed.
Files changed: internal/config/config.go, internal/config/config_test.go.
