VERDICT: ACCEPT

The patch meets the whitespace splitting requirements for scalar `[]string` values, including empty strings and equivalent YAML and ENV inputs. Existing sequence values remain unchanged.

`GOPROXY=off GOSUMDB=off go test ./internal/config` passed. `git diff --check` passed. No code defects or TEST_ENVIRONMENT_PROBLEM found.