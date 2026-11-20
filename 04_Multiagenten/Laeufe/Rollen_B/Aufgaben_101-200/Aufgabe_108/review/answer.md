VERDICT: ACCEPT

The applied patch provides the typed cache interface in [simple_cache.go](/app/utils/cache/simple_cache.go) and updates the affected callers. I found no correctness or regression defect.

`GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./utils/cache ./scanner ./core/scrobbler` passed for all three packages. `git diff --check` passed, and `gofmt -d` produced no changes. TEST_ENVIRONMENT_PROBLEM: none.