Task: Add HTTPS support to Flipt configuration and serving endpoints.
Status: Complete. Per-call YAML/environment configuration, HTTPS validation, REST/UI and gRPC TLS serving, documentation, and focused tests are implemented.
Verification: GOPROXY=off go test ./... passed; git diff --check passed.
Constraints followed: Local code and tests only; no git history, index baseline, or harness configuration changes.
