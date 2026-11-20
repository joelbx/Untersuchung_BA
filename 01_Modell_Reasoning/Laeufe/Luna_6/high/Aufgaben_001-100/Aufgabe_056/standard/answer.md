Implemented Safari 17+ HEIC/HEIF and JXL support on macOS and iOS, added the JXL MIME type and extension mapping, and simplified file MIME detection in both Drive parser copies.

Verification: the existing Drive media test and shared lint passed. The shared type check hit an unrelated `openpgp` type mismatch in `packages/crypto/lib/worker/api.ts`.

Key changes: [mimetype.ts](/app/packages/shared/lib/helpers/mimetype.ts), [constants.ts](/app/packages/shared/lib/drive/constants.ts), [Drive MIME parser](/app/packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.ts).