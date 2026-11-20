# Work checkpoint

Task: add HEIC/JXL image support for Safari 17+ and simplify MIME detection.

Implemented: JXL enum and extension override; HEIC/JXL compatibility checks for macOS/iOS Safari 17+; conditional image support for HEIC, HEIF and JXL; simplified MIME selection in both Drive parser copies without ChunkFileReader. Added regression tests for supported and unsupported browsers and file type/extension fallback.

Verified: 3 Drive store suites pass (17 tests); ESLint passes for changed files with a 4 GB Node heap; parser copies match; git diff --check passes. Shared and Drive store type checks report existing errors in crypto, documents, config imports, but none in changed files.
