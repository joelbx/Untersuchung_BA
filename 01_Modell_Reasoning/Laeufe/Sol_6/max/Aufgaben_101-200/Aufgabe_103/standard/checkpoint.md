# Checkpoint

Resolved RPM package parsing in `scanner/redhatbase.go` and added regression coverage in `scanner/redhatbase_test.go`.

- Preserve empty release fields in installed RPM and repoquery output.
- Use a shared epoch/version/release formatter for source and update candidate versions.
- Parse both `.src.rpm` and `-src.rpm` source filenames, including empty releases; reject malformed filenames.
- Verified with `GOPROXY=off GOSUMDB=off go test ./scanner -count=1` (passed).

No git history or index changes were made.
