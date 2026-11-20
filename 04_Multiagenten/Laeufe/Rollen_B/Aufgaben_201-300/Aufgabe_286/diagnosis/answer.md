I located the fault, but the specialist instructions for this task prohibit source and test edits, so the issue remains unresolved. I recorded the findings in [checkpoint.md](/app/.codex-role-output/checkpoint.md).

- [main.go](/app/cmd/flipt/main.go:383) treats `-rc` as a release: `isRelease()` excludes only empty versions, `dev`, and `-snapshot`.
- [main.go](/app/cmd/flipt/main.go:214) owns the release lookup, version comparison, status messages, and telemetry gating. The requested `internal/release/check.go` does not exist yet.
- For a nonrelease build, [main.go](/app/cmd/flipt/main.go:276) puts zero-value semantic versions (`0.0.0`) into `info.Flipt`. The [metadata struct](/app/internal/info/flipt.go:8) already has fields for version, latest version, release status, and update availability.
- CI values `true` and `1` already disable telemetry. Nonrelease builds skip reporter initialization, but do not emit the required debug message.

The fix should centralize classification and update checking in `release.Is` and `release.Check`, use the returned `release.Info` for both output modes and metadata, and keep startup running when a check fails while logging `"checking for updates"` with the error. I found no existing release or `cmd/flipt` tests; suffix behavior beyond the specified examples remains an implementation detail to verify.