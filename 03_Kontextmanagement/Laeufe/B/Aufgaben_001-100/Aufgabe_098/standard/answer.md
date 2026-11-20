Updated telemetry to version **1.3** and added an optional `audit.sinks` array containing `log`, `webhook`, or both when enabled. The audit field is omitted when neither sink is enabled.

The existing telemetry package tests pass, including the new sink combinations. `git diff --check` passes.