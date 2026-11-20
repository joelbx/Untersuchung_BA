# Checkpoint

Task: add Safari 17+ HEIC/JXL image capability support and simplify MIME detection.

Implemented:
- Added `image/jxl` and the `jxl` extension mapping.
- Added Safari 17+ detection for macOS/iOS and used it to gate HEIC/HEIF and JXL in supported image detection.
- Removed `ChunkFileReader` from `mimeTypeFromFile`; specific browser MIME types take priority, with filename extension lookup as fallback for missing or generic MIME values.
- Kept the Drive application parser copy synchronized with the drive-store source.

Verification:
- Existing Drive media test passed.
- Shared package lint passed.
- Shared package type check reached an unrelated pre-existing `openpgp` type mismatch in `packages/crypto/lib/worker/api.ts`.
