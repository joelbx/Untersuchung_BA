# OCI manifest version issue

Status: complete. Implemented the OCI manifest version field, 1.1 default, validation, store option, and wiring through server and bundle command. Added config fixtures and a manifest output test.

Verification: `go test ./internal/config ./internal/oci`; `go test ./config ./internal/storage/fs/store ./cmd/flipt`; `go test ./internal/config` after validation cleanup; `git diff --check`. All passed with Go network access disabled.

Constraints: local repository only; preserve git history, index baseline, and harness configuration.
