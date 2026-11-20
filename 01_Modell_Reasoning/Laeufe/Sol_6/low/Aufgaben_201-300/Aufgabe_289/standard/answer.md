I added `DefaultConfig` and exported `DecodeHooks`, and updated `Load` to compose those same hooks. I also changed storage’s `Local` and `Git` fields to pointers and added nil checks for their validation paths.

`go test ./internal/config` passes, and `git diff --check` is clean. The broader `internal/cmd` test run was still running when I finished, so CUE validation remains unconfirmed.