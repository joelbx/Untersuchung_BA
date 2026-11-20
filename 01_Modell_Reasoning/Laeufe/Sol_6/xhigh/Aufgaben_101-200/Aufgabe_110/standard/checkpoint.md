# Download mechanism metric checkpoint

- Started tracing the Drive download flows, file saver mechanism selection, and metric schemas.
- Working tree was clean at start.
- Added the `web_drive_download_mechanism_success_rate_total_v1` schema and registered its counter in the metrics package.
- Shared mechanism selection between the file saver and terminal download metrics; stateful downloads use `meta.size`, and previews report `link.size`.
- Preserved known single-file size when the saver size wait expires and treated missing service-worker capability as memory fallback.
- Validation passed: focused Drive metrics tests (21), metrics Counter test (1), Drive and metrics TypeScript checks, ESLint, Prettier, and `git diff --check`.
