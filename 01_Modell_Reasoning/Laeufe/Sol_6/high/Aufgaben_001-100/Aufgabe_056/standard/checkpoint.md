# Checkpoint

Task: add Safari 17+ HEIC/JXL image support and simplify upload MIME detection.

Findings: shared image capability checks are in `packages/shared/lib/helpers/mimetype.ts`; MIME parsing exists in both Drive application and drive-store package upload paths.

Implemented: JXL enum and extension mapping, Safari 17+ macOS/iOS checks for HEIC and JXL, and file type then extension MIME resolution without `ChunkFileReader` in both upload paths. Added focused tests for browser support and MIME fallback.

Verification: drive-store focused Jest suites passed (11 tests); Drive application media Jest suite passed (1 test); ESLint, Prettier, and `git diff --check` passed on edited files. Drive-store type checking reports five unrelated existing errors in crypto, documents, and missing config imports; none reference the changed files.
