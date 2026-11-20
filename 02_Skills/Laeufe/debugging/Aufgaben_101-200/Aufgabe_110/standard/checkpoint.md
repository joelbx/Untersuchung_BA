# Checkpoint

Task: add mechanism segmented download outcome metric.
Status: investigating download mechanism selection and metric reporting paths.
Constraint: local repository only; no downloads or external research.

Investigation: `useDownloadMetrics` emits the existing success counter at Done/Error/NetworkError, but has no mechanism counter or size argument for preview reports. Queue initializes `meta.size` from a file link and updates it on `onInit`; preview `downloadStream` has `link.size` but drops it in `report`. FileSaver chooses memory via a truthy `meta.size` comparison, so zero bypasses memory; service-worker fallback is tracked by `useBlobFallback` after registration failure. New metric must be registered in `Metrics.ts` as a Counter using the web-prefixed schema name, which generates the `drive_...` property.

Hypothesis: adding one shared selector tied to FileSaver's threshold/capability/fallback state, then passing `meta.size` or `link.size` to terminal reporting, will produce labels consistent with saving decisions. Test first.

Regression evidence: initial focused Jest run failed in the two new metric tests with zero calls to `drive_download_mechanism_success_rate_total.increment`; existing tests passed. A minimal static assertion also failed because the increment was absent. After the patch, focused Jest passed (2 suites, 21 tests), metrics TypeScript check passed, Prettier check passed, ESLint check passed, and `git diff --check` passed. Drive TypeScript check remains in progress.

Final verification: the first Drive TypeScript check failed with TS2739 in the new test fixture (`meta` lacked filename and mimeType). After correcting the fixture, Drive `tsc --noEmit --pretty false` passed. Focused Jest passed again (2 suites, 21 tests). Metrics TypeScript check passed. ESLint (`--quiet`), Prettier check, and `git diff --check` passed. No external tooling or downloads were used.
