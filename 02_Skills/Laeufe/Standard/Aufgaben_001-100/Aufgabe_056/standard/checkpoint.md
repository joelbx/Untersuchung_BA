# Checkpoint

Issue: Safari 17+ HEIC/JXL thumbnail and preview support; simplify MIME detection.
Status: implementation complete.

Changed:
- MIME selection uses the file's specific type first, then extension lookup for missing or generic types. Removed ChunkFileReader dependency.
- Added image/jxl enum and jxl extension mapping.
- Added HEIC/HEIF and JXL image support gated on Safari or Mobile Safari 17+ on Mac OS or iOS.
- Added focused browser and MIME tests.

Checks:
- `node_modules/.bin/jest --config packages/drive-store/jest.config.js --runInBand --coverage=false packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.test.ts packages/drive-store/store/_uploads/media/image.test.ts`: passed, 2 suites / 14 tests.
- `node_modules/.bin/prettier --check packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.ts packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.test.ts packages/shared/lib/drive/constants.ts packages/shared/lib/helpers/mimetype.ts`: passed.
- `git diff --check`: passed.
- `node_modules/.bin/tsc --noEmit -p packages/drive-store/tsconfig.json`: exit 2, still fails in untouched files: TS2345 in packages/crypto/lib/worker/api.ts:579 (two OpenPGP PartialConfig versions incompatible); TS2724 in packages/drive-store/lib/_documents/useDocuments.ts:16 (missing encryptExtendedAttributes); TS2339 in packages/drive-store/lib/_documents/useOpenDocument.ts:22 (missing PROTONDOCS); TS2307 in packages/drive-store/store/_downloads/download/downloadBlock.ts:12 and packages/drive-store/store/_uploads/worker/upload.ts:10 (missing ../../../config). No diagnostics in changed files after correcting test mocks. Full package type status remains uncertain because of these existing errors.

Tool note: `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find.
