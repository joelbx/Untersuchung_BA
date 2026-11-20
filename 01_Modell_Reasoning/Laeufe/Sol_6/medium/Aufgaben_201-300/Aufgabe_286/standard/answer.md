Moved release classification and update checking into `internal/release`. Startup now treats `-rc`, snapshot, and dev builds as non-releases, reports update status from `release.Info`, and disables telemetry for non-release builds or CI. Failed update checks warn and do not stop startup.

Targeted tests passed for release checking, startup compilation, telemetry, and config.