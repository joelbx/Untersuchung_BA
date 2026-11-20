# Checkpoint

Implemented HEIC and JXL thumbnail and preview support in the shared MIME helper and both Drive upload MIME parsers.

- Added `image/jxl` and a `.jxl` extension mapping.
- HEIC/HEIF variants and JXL are accepted for previews and thumbnails on macOS/iOS Safari 17+.
- Upload MIME parsing now prefers a specific `File.type`, then uses the extension when the type is empty or generic. Both Drive copies are updated.
- Relevant Drive Jest suites pass (13 tests); Prettier and ESLint pass on changed files.
- Shared Karma suite cannot launch because its configured Playwright Chromium binary is missing. Shared and drive-store TypeScript checks report existing errors in untouched crypto and drive-store files; no errors remain in changed files.
