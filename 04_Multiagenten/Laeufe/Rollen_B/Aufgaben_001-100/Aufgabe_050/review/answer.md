VERDICT: ACCEPT

The checked-out patch handles the nullable fields in the issue. `P` preserves zero values as pointers, `V` returns zero values for nil pointers, and the affected timestamp and `image_files` reads and assignments use those helpers. I found no correctness regression.

`GOPROXY=off GOSUMDB=off go test ./utils/gg ./persistence ./core/... ./scanner ./server/public ./server/subsonic` passed (exit 0). `git diff --check` also passed. TEST_ENVIRONMENT_PROBLEM: none.