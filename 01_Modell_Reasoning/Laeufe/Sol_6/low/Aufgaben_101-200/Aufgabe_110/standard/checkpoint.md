Task: add download mechanism outcome metric in Drive.
Status: tracing downloader, metrics hook, and existing schema/tests.
Implemented selector, schema, counter registration, hook emission, and preview size propagation. Testing next.
Verification: useDownloadMetrics.test.ts passed (16/16); git diff --check passed.
