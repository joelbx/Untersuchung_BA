Implemented Safari 17+ HEIC/HEIF and JXL support on macOS and iOS in [mimetype.ts](/app/packages/shared/lib/helpers/mimetype.ts:61). Added `image/jxl` and its extension mapping in [constants.ts](/app/packages/shared/lib/drive/constants.ts:119).

Simplified `mimeTypeFromFile` in both Drive parser copies: it uses a specific `File.type` when available, otherwise falls back to the filename extension.

Both Drive media test suites passed: 2 suites and 6 tests in each workspace. `git diff --check` passed.