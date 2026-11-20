Task: Fix authentication database initialization and cleanup for JWT with non-database storage.
Status: Implemented and verified.
Changes: Per-method RequiresDatabase metadata; AuthenticationConfig.RequiresDatabase and cleanup gating; conditional auth SQL/store/cache initialization with JWT middleware preserved; cleanup skips disabled and non-database methods; regression tests for method combinations and JWT startup on local, Git, OCI, and object storage.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/cmd ./internal/config ./internal/cleanup (passed); git diff --check (passed).
Delegation: None.
