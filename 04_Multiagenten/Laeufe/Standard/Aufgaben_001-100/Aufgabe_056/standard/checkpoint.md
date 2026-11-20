# Checkpoint

Task: Add HEIC/JXL thumbnail and preview support on macOS/iOS Safari 17+ and simplify MIME detection.

Completed:
- Added JXL MIME enum and extension mapping.
- Added Safari 17+ Apple OS guards for HEIC/HEIF and JXL image support.
- Simplified both checked-out upload MIME parsers to use a specific File.type or extension lookup.
- Added parser and browser compatibility tests.

Verification:
- Three relevant Jest suites passed (10 tests).
- Prettier check and git diff --check passed.
- Shared and drive-store type checks fail on existing unrelated errors in crypto/lib/worker/api.ts and drive-store documents/config files.
