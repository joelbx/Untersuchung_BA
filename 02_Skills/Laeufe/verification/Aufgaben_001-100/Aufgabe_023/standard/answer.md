Authentication now opens a database only when an enabled method requires one. JWT uses in-memory auth storage with Local, Git, or OCI flag storage, and its interceptor still initializes. Cleanup runs only for enabled methods that require a database.

Verification passed: `GOPROXY=off GOSUMDB=off go test -count=1 ./internal/config ./internal/cmd ./internal/cleanup` and `git diff --check`.