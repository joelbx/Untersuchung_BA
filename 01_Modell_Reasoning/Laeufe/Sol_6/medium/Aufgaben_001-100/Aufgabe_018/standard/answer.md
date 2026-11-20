Fixed configuration decoding so scalar strings for `[]string` fields split on whitespace, with repeated whitespace ignored and empty strings producing an empty slice. The hook applies only to string sources and `[]string` targets.

Updated the CORS fixture and tests to cover YAML and ENV loading, plus empty values and pass-through behavior. `GOPROXY=off go test ./internal/config` passed.