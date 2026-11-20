# Checkpoint

Issue: add opt-out anonymous telemetry with persistent host UUID, periodic reporting, and an HTTP JSON handler for internal info.

Plan: inspect config/defaults and application startup/logging/version patterns; implement state management and reporting using repository dependencies; wire startup with cancellation; update advanced config; run existing relevant tests.
