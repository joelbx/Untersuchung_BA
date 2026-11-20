HTTPS support is implemented for the REST API, UI, and gRPC endpoints. Configuration now supports protocol selection, separate HTTP and HTTPS ports, certificate paths, and the required startup validation while retaining HTTP defaults.

`GOPROXY=off go test ./...` and `git diff --check` pass. The build still emits a warning from the existing sqlite3 C dependency.