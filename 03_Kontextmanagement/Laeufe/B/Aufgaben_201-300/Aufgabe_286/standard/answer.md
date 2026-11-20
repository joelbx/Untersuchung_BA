Resolved the startup release and update issue. Release candidates such as `-rc` are now classified as non-release builds; startup uses `release.Info` for update messages and disables telemetry for non-release builds or CI.

Relevant Go tests passed, including new release classification and update-check tests.