Implemented HTTPS support with `http`/`https` protocol configuration, separate web ports, TLS credential validation, and TLS for both the web and gRPC listeners. Updated defaults and configuration documentation.

`go test ./...` and `git diff --check` passed. The test run showed a compiler warning in the existing sqlite3 C code; all Go packages passed.

Key changes: [config.go](/app/cmd/flipt/config.go:14), [main.go](/app/cmd/flipt/main.go:291), [configuration docs](/app/docs/configuration.md:24).