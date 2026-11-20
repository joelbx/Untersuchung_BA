Task: HEIC/JXL thumbnail and preview support on macOS/iOS Safari 17+.
Status: implementation complete; focused regression tests pass.
Changes: added JXL MIME/extension mapping; added Safari 17+ Apple OS capability checks for HEIC variants and JXL; made both Drive MIME parsers prefer File.type and fall back to extension without ChunkFileReader.
TDD: wrote imageSupport.test.ts and mimeTypeParser.test.ts before production edits. Initial focused Jest run: 8 expected failures and 4 passes; subsequent focused run: 12 passes.
Checks:
- ./node_modules/.bin/jest --config packages/drive-store/jest.config.js --runInBand --coverage=false packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.test.ts packages/drive-store/store/_uploads/mimeTypeParser/imageSupport.test.ts: PASS, 12 tests.
- ./node_modules/.bin/jest --config packages/drive-store/jest.config.js --runInBand --coverage=false: FAIL, 4 suites cannot find ../../../config from existing downloadBlock.ts/upload.ts; 56 suites pass, 422 tests pass and 4 skipped. Uncertainty: remaining four suites could not execute.
- ./node_modules/.bin/tsc --noEmit -p packages/shared/tsconfig.json: FAIL, existing packages/crypto/lib/worker/api.ts:579 openpgp type mismatch.
- ./node_modules/.bin/tsc --noEmit -p packages/drive-store/tsconfig.json: FAIL, same crypto mismatch plus existing missing encryptExtendedAttributes, PROTONDOCS, and ../../../config references. No diagnostics in edited files.
- ./node_modules/.bin/karma start packages/shared/test/karma.conf.js: FAIL after successful webpack build; ChromeHeadless binary missing at /root/.cache/ms-playwright/chromium-1105/chrome-linux/chrome. Shared suite unexecuted.
- git diff --check: PASS.
