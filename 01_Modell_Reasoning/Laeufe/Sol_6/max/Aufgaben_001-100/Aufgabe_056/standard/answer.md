Implemented HEIC/HEIF and JXL thumbnail and preview support for macOS and iOS Safari 17+. [mimetype.ts](/app/packages/shared/lib/helpers/mimetype.ts) now checks browser compatibility, and [constants.ts](/app/packages/shared/lib/drive/constants.ts) defines `image/jxl` and maps `.jxl` to it.

Both Drive upload parsers now use a specific `File.type` first, then the filename extension when the type is missing or generic. Thirteen targeted Jest tests pass; ESLint and Prettier pass.

The shared Karma suite could not start because its Chromium binary is missing. TypeScript checks still report errors in untouched crypto and drive-store files, with none in the changed files.