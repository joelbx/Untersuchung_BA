Task: implement anonymous opt-out telemetry in Flipt.
Completed: config defaults/env parsing; state directory and persistent UUID/timestamp; 4-hour background reporting; startup integration; internal/info.Flipt handler; advanced example opt-out; unit coverage.
Verification: GOPROXY=off go test ./config ./telemetry ./internal/info ./cmd/flipt passed; git diff --check passed.
Constraints respected: local code/tests only; no git history/index/harness changes.
