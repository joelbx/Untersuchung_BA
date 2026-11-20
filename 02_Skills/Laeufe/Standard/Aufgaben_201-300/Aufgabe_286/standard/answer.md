Startup now uses `release.Is(version)` and `release.Check(ctx, version)`. Release candidates and other prerelease builds are treated as non-releases, so telemetry is disabled for them. Update messages use the returned release information, and a failed check logs a warning while startup continues.

The release, startup, telemetry, and config package tests passed with offline Go tooling.