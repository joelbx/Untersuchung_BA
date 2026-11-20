# Checkpoint

Objective completed: Add mechanism-segmented terminal download outcome metrics using `drive_download_mechanism_success_rate_total`.

Implemented:
- `selectMechanismForDownload(size)` selects memory below the configured limit, memory fallback when service workers are unavailable, and service worker otherwise; FileSaver uses the selector to choose its path.
- The v1 metric is registered under backend name `web_drive_download_mechanism_success_rate_total` with `status`, `retry`, and `mechanism` labels.
- Stateful terminal outcomes use `meta.size`; preview reports pass `link.size`; retry status comes from the observed retry count.
- Service-worker capability detection is shared by the saver and selector.

Verification passed:
- Focused Drive `useDownloadMetrics` suite: 17 tests.
- Metrics package suite: 107 tests across 8 suites.
- Drive and metrics package type checks.
- `git diff --check`.
