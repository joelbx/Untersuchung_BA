# Telemetry implementation checkpoint

Task: add opt-out anonymous telemetry with persisted host UUID, four-hour reporting, and HTTP JSON for Flipt info.

Status: implemented configuration, persisted telemetry reporter, server startup integration, and Flipt info handler. Full Go test suite and telemetry/info race tests pass.

Collector: default URL is `https://telemetry.flipt.io/v1/track`; `meta.telemetry_endpoint` and `FLIPT_META_TELEMETRY_ENDPOINT` can override it. External endpoint availability could not be verified locally.
