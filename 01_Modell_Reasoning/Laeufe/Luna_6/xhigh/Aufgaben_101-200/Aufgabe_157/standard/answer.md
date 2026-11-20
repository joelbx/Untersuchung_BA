Implemented the mail metrics helpers in [mailMetricsHelper.ts](/app/applications/mail/src/app/metrics/mailMetricsHelper.ts). Custom mailbox IDs map to `"custom"`, built-in IDs are preserved, and page sizes map to `"50"`, `"100"`, or `"200"`, defaulting to `"50"`.

Added `@proton/metrics` to the mail app manifest and [yarn.lock](/app/yarn.lock).

Verification passed: mail app type checking and both existing test suites (37 tests). Updated the checkpoint at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).