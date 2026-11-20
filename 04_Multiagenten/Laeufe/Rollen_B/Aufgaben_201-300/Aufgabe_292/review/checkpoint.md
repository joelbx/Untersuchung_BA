VERDICT: FIX

Code defects:
- internal/storage/fs/poll.go:103-112: Close only waits when Poll has already set running. Each constructor starts Poll in a new goroutine, so an immediate Close can return while that goroutine is still pending. Arrange start registration before launching it, and wait for the goroutine's completion in every Close path.
- internal/storage/fs/store.go:35-40 and internal/storage/fs/store/store.go:92,99,130,161,175: the application factory wraps snapshot stores in fs.Store, which does not expose or forward Close. Add a Close method on the wrapper that forwards to the underlying backend so callers can stop polling through the returned store.

Tests:
- GOPROXY=off GOSUMDB=off go test ./internal/storage/fs/... : exit 0; fs, git, local, azblob, blob, s3, and oci packages passed; fs/store has no test files.
- GOPROXY=off GOSUMDB=off go test -v -run '^Test_Store$' ./internal/storage/fs/git ./internal/storage/fs/object/azblob ./internal/storage/fs/object/s3 : exit 0; git had no matching test, Azure and S3 tests skipped because TEST_AZURE_ENDPOINT and TEST_S3_ENDPOINT are unset.
- GOPROXY=off GOSUMDB=off go test -v -run '^Test_Store_Subscribe$' ./internal/storage/fs/git : exit 0; skipped because TEST_GIT_REPO_URL is unset.

TEST_ENVIRONMENT_PROBLEM: Integration polling behavior for Git, Azure, and S3 could not be exercised without their existing test services and endpoint settings. No project code was changed during review.
