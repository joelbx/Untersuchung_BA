# Checkpoint

Issue: add mechanism-segmented download outcome metric.

Implemented `selectMechanismForDownload` and aligned file saver behavior; added and registered the `web_drive_download_mechanism_success_rate_total_v1` schema; emitted status, retry, and mechanism from `useDownloadMetrics`; propagated preview size through `report`; added focused tests.

Verification: 21 focused Drive tests passed; Drive and metrics type checks passed; ESLint on changed source files passed; `git diff --check` passed.
