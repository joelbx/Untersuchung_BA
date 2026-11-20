Implemented mechanism segmented download metrics. The new counter records `status`, `retry`, and the selected mechanism; file size now reaches the metric from stateful downloads and previews. Added the schema type and mirrored the Drive store changes in `packages/drive-store`.

Verification passed: the targeted `useDownloadMetrics` Jest suite, Drive TypeScript check, and `git diff --check`.