I localized the HTTPS gap, but did not implement a fix: this run’s fault-localization instruction prohibits changes to project source and tests.

- [config.go](/app/cmd/flipt/config.go:39) has no `Scheme`, HTTPS port, certificate fields, or TLS validation. `configure()` takes no path argument and wraps load errors, so it does not meet the required interface or error behavior.
- [main.go](/app/cmd/flipt/main.go:268) starts gRPC without TLS credentials. The REST gateway dials it insecurely, and REST/UI always serves HTTP on `HTTPPort` ([main.go](/app/cmd/flipt/main.go:309)).
- Both configuration and information handlers already write non-empty JSON with an implicit `200 OK` response ([config.go](/app/cmd/flipt/config.go:171)).

The fix needs to cover HTTPS selection and certificate checks, TLS for the selected listeners and gateway connection, and unchanged HTTP defaults. I found no tests in `cmd/flipt`; `go test ./cmd/flipt` passed as a compile check. I recorded the diagnosis in [checkpoint.md](/app/.codex-role-output/checkpoint.md).