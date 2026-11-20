Implemented HEIC/JXL image support and MIME detection updates.

- Added `image/jxl` to [constants.ts](/app/packages/shared/lib/drive/constants.ts) and mapped `.jxl` to that MIME type.
- Added Safari 17+ checks for macOS and iOS in [mimetype.ts](/app/packages/shared/lib/helpers/mimetype.ts), and gated HEIC/HEIF variants and JXL in supported image detection.
- Simplified MIME detection in both Drive parser copies to prefer a useful `File.type`, then use the filename extension when the type is missing or generic.

**Verification:** Drive thumbnail scaling and media info tests passed. The shared browser suite could not start because its Playwright Chromium binary is missing. Shared and Drive Store type checks reported errors in unrelated crypto, documents, and Drive config code.