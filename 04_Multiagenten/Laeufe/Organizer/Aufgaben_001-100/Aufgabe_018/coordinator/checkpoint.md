Task: Fix scalar string to []string configuration decoding for YAML and ENV.
Status: Complete. Replaced comma separator hook with a typed whitespace hook using strings.Fields; enabled explicit empty ENV values; updated advanced fixture; added direct hook and load tests.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/config -count=1 passed. git diff --check passed.
Delegation: None.
