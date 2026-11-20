# Checkpoint

Implemented `drive_download_mechanism_success_rate_total` with `status`, `retry`, and `mechanism` labels; added its schema type and registered the v1 counter in `packages/metrics/Metrics.ts`.

Added `selectMechanismForDownload(size)` using the configured memory threshold and service worker support. Stateful downloads pass `meta.size`; preview reports pass the link size. The implementation is mirrored in `packages/drive-store`.

Verification passed:
- `yarn workspace proton-drive test --runInBand src/app/store/_downloads/DownloadProvider/useDownloadMetrics.test.ts`
- `yarn workspace proton-drive check-types --pretty false`
- `git diff --check`
