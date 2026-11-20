Task: implement gRPC x-flipt-accept-server-version handling in /app.
Status: implemented and verified targeted middleware tests and internal/cmd tests via full suite.
TDD red: GOPROXY=off GOSUMDB=off go test ./internal/server/middleware/grpc -run 'TestFliptAcceptServerVersion|TestWithFliptAcceptServerVersion' -count=1 failed to build as expected because the three new API functions were undefined.
Green: same focused command passed. GOPROXY=off GOSUMDB=off go test ./internal/server/middleware/grpc -count=1 passed.
Full suite: GOPROXY=off GOSUMDB=off go test ./... exited 1. Failures: internal/cache/redis TestSet, TestGet, TestDelete cannot connect to Docker daemon at unix:///var/run/docker.sock; internal/gitfs Test_FS_Submodule remote Git GET returned Forbidden. Other packages, including internal/cmd and middleware/grpc, passed. Full-suite green status remains unverified in this environment because these tests require unavailable external services.
Go generated go.work.sum additions during tests; restored the original worktree version after the run.
