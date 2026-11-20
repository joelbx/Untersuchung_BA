# Configuration metadata issue

- Task: add metadata configuration for startup version checking with an enabled default.
- Status: implemented metadata.check_for_updates with a true default; YAML and JSON loading verified.
- Verification: `GOPROXY=off GOSUMDB=off go test ./config` and `GOPROXY=off GOSUMDB=off go test ./...` passed.
