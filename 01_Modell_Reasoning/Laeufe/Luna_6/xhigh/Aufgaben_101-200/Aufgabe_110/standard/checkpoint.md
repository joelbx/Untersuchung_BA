# Checkpoint

Task: add mechanism-segmented terminal download outcome metrics and deterministic mechanism selection.

Implemented:
- Added `selectMechanismForDownload(size)` in the file saver. It selects `memory` below `MEMORY_DOWNLOAD_LIMIT`, and otherwise selects `memory_fallback` when service worker support/setup is unavailable or `sw` when available. File saver routing uses the same selection.
- Registered `web_drive_download_mechanism_success_rate_total` v1 with status, retry, and mechanism labels and wired the application counter as `drive_download_mechanism_success_rate_total`.
- Stateful terminal outcomes use `meta.size`; preview terminal reports pass the link size. Retry labels use the download retry count, and preview reports use `false`.
- Updated existing hook tests for mechanism labels and size forwarding.

Verification:
- Focused Drive metrics hook suite: 17 tests passed.
- `yarn workspace @proton/metrics check-types`: passed.
- `yarn workspace proton-drive check-types`: passed.
- ESLint on changed TypeScript files: passed.
- `git diff --check`: passed.
