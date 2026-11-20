Fixed startup release and update handling. `release.Is` now excludes `dev`, snapshot, release candidate, and other prerelease builds. Startup uses `release.Check` results for update messages and metadata, and disables telemetry for non-release builds or when `CI` is `true` or `1`. Update check failures log a warning and allow startup to continue.

Relevant tests and `git diff --check` pass.