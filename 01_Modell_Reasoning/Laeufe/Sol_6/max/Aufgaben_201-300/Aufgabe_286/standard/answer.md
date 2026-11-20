Resolved the startup release check issue. [release.Is](/app/internal/release/check.go:33) now treats `-rc`, `-snapshot`, `dev`, and other prerelease versions as non-release builds. [release.Check](/app/internal/release/check.go:45) owns the update comparison and logs a warning on failure; startup continues.

[Startup](/app/cmd/flipt/main.go:212) now uses the returned release information for console or logger status messages and [metadata](/app/internal/info/flipt.go:8), and disables telemetry for non-release builds or when `CI` is `true` or `1`.

Relevant tests passed with network access disabled.