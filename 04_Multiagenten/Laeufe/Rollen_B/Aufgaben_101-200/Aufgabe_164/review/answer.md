VERDICT: ACCEPT

The applied patch addresses the reported YAML metadata and JSON header import failures. Review of [encoding.go](/app/internal/ext/encoding.go) and [importer.go](/app/internal/ext/importer.go) found no correctness or regression issue; the existing tests cover nested metadata, attachments, and namespace key, name, and description.

`go test ./internal/ext ./cmd/flipt` passed (`internal/ext` passed; `cmd/flipt` has no test files). `git diff --check` passed. No project code was changed during this review.