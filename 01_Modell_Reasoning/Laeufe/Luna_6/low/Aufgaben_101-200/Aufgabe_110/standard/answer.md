Implemented the mechanism segmented download metric across both Drive downloader source trees. Terminal stateful and preview downloads now emit status, retry, and mechanism labels. The selector uses the downloader’s service worker support rules, and the file saver exposes `selectMechanismForDownload(size)`.

Registered the counter in [Metrics.ts](/app/packages/metrics/Metrics.ts) and added its schema type at [web_drive_download_mechanism_success_rate_total_v1.schema.d.ts](/app/packages/metrics/types/web_drive_download_mechanism_success_rate_total_v1.schema.d.ts).

Verification: metrics type checking and `git diff --check` passed. The targeted Drive test and application type check produced no output during startup, so I stopped them; their results are inconclusive.