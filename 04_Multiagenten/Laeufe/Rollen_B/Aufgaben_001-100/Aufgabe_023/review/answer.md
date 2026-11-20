VERDICT: ACCEPT

The patch sets `RequiresDatabase` for every supported authentication method and uses it to gate database initialization and cleanup. I found no correctness or regression issue in the reviewed paths.

`go test ./internal/config ./internal/cmd ./internal/cleanup` passed for all three packages. TEST_ENVIRONMENT_PROBLEM: none.