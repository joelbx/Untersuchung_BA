# Checkpoint

Implemented the download mechanism counter in both Drive downloader source trees. The metric emits status, retry, and mechanism labels for terminal stateful and preview downloads; the file saver exposes `selectMechanismForDownload(size)` and uses the same selection for its buffering decision. Registered the counter in `packages/metrics/Metrics.ts` and added the generated schema type under `packages/metrics/types`.

Verification: `yarn workspace @proton/metrics check-types` passed; `git diff --check` passed. The targeted Drive Jest test and Drive application type check produced no output during startup and were stopped after continued silence, so they are inconclusive.
