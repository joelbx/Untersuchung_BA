# Download mechanism metric checkpoint

Task complete: added mechanism-segmented terminal download outcome metric for Drive.

Changes:
- FileSaver exposes `selectMechanismForDownload(size)` and uses the same selection when saving. It accounts for the memory threshold, unsupported service workers, and failed service worker initialization.
- Metrics package defines `web_drive_download_mechanism_success_rate_total_v1` labels and registers the v1 counter as `drive_download_mechanism_success_rate_total`.
- `useDownloadMetrics` emits status, retry, and mechanism for terminal stateful downloads using `meta.size`, and preview reports pass `link.size`.
- Buffered queue downloads reach Done only after saving succeeds; save errors reach Error. Cancellation remains terminal.
- Added selector and hook tests and a metrics backend contract check.

Validation:
- Drive focused tests: 20 passed.
- Metrics integration tests: 17 passed.
- Drive and metrics type checks: passed.
- Prettier and git diff checks: passed.
- ESLint: 0 errors, 5 existing warnings in touched files.
