Moved release classification and update checking into `internal/release`. Startup now uses `release.Info` for version messages, treats `-rc` and other prereleases as non-release builds, and disables telemetry for those builds and for CI. A failed update check logs a warning and lets startup continue.

The release checks and relevant existing Go tests passed.