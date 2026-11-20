Added HTTPS support for REST, UI, and gRPC. Configuration now supports `server.protocol`, `https_port`, `cert_file`, and `cert_key`, with HTTP defaults preserved and HTTPS certificate paths validated at startup. Updated the configuration docs and added tests for defaults, overrides, validation, and metadata responses.

`GOPROXY=off go test ./...` and `git diff --check` passed.