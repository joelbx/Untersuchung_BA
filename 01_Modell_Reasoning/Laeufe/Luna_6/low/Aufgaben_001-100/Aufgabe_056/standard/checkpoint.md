Task: Resolve HEIC/JXL image support and simplify MIME detection.

Implemented:
- Added JXL MIME enum and extension mapping.
- Added macOS/iOS Safari 17+ capability checks using Version.isGreaterThanOrEqual for HEIC/HEIF and JXL; included conditional support in isSupportedImage.
- Removed ChunkFileReader usage from mimeTypeFromFile. MIME now comes from a recognized filename extension first, with input.type and application/octet-stream fallbacks.

Verification:
- Prettier check and git diff --check passed.
- Drive-store lint and workspace type checks were run but report existing unrelated errors (unresolved config imports; shared/crypto OpenPGP type mismatch; other pre-existing drive-store type errors).
