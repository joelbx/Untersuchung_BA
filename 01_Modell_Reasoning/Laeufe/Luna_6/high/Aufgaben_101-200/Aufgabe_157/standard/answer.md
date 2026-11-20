Implemented the mail metrics helpers in [mailMetricsHelper.ts](/app/applications/mail/src/app/metrics/mailMetricsHelper.ts). Custom labels and folders now map to `"custom"`; built-in mailbox IDs are preserved. Page sizes map to `"50"`, `"100"`, or `"200"`, with `"50"` as the fallback.

Added `@proton/metrics` to the mail app manifest and lockfile.

Validation passed: mail workspace type check, existing label tests, and `git diff --check`.