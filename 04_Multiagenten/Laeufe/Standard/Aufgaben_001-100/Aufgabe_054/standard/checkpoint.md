# Checkpoint

Task: add generic singleton.GetInstance with per-type caching and concurrency safety.
Status: implemented and verified.
Tests: GOPROXY=off GOSUMDB=off go test ./utils/singleton; GOPROXY=off GOSUMDB=off go test -race ./utils/singleton.
