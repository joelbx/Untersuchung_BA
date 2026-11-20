Implemented mechanism-segmented download outcome metrics. The file saver and metrics hook share [selectMechanismForDownload](/app/applications/drive/src/app/store/_downloads/fileSaver/fileSaver.ts:20), selecting `memory`, `sw`, or `memory_fallback`.

The hook now records status, retry, and mechanism labels for terminal downloads. Queued downloads use `meta.size`; preview reports pass the link size. The counter is registered as `drive_download_mechanism_success_rate_total` with the v1 schema in [Metrics.ts](/app/packages/metrics/Metrics.ts:351) and [the schema type](/app/packages/metrics/types/web_drive_download_mechanism_success_rate_total_v1.schema.d.ts:11).

**Verification:** focused suite passed (17 tests); Drive and metrics type checks, ESLint, and `git diff --check` passed.