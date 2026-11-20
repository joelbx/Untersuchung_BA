Implemented the metrics helpers in [mailMetricsHelper.ts](/app/applications/mail/src/app/metrics/mailMetricsHelper.ts): custom labels and folders map to `"custom"`, built-in IDs are preserved, and page sizes normalize to `"50"`, `"100"`, or `"200"` with `"50"` as the fallback.

Added `@proton/metrics` to the mail app manifest and [yarn.lock](/app/yarn.lock:35942).

Verification passed: mail app typecheck, existing labels test (24 cases), and `git diff --check`.