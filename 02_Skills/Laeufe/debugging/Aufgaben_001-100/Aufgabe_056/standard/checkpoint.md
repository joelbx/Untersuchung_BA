# Debugging checkpoint

Task: Add conditional HEIC/JXL image support for Safari 17+ and simplify MIME detection.

Phase 1 in progress. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep`.

Root cause: both Drive parser copies gate extension lookup on a 4,100-byte reader check; small files return octet-stream even with a known extension or explicit MIME type. The shared image whitelist omits HEIC and JXL. JXL is absent from the enum and extension map. Browser helpers expose Safari name/version and OS name; Version supports semantic >= comparisons.

Pattern: AVIF support in shared mimetype.ts gates by browser/version. Drive parser is duplicated from applications/drive into packages/drive-store by its sync script.

Hypothesis: removing the reader gate, prioritizing meaningful File.type then extension, and adding Safari 17+ OS checks resolves the issue. Regression test run before fix: `./node_modules/.bin/jest --config packages/drive-store/jest.config.js --runInBand packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.test.ts`; failed as expected (octet-stream for both cases).

Verification limitation: `./node_modules/.bin/karma start packages/shared/test/karma.conf.js --single-run` bundled successfully but exited 1: `Cannot start ChromeHeadless: Can not find the binary /root/.cache/ms-playwright/chromium-1105/chrome-linux/chrome`. Shared Jasmine tests were not executed. Using installed Jest for equivalent browser-gate coverage.

Tooling: the broad ESLint invocation hit Node's 2 GB heap limit (`FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory`) while two project typechecks were active; stopped that lint process. Will use smaller sequential checks. Jest browser-gate and parser tests passed (7 tests), then added an octet-stream fallback test to rerun.

Typechecks: `./node_modules/.bin/tsc --project packages/shared/tsconfig.json --noEmit --pretty false` exited 2 for an existing crypto/openpgp type mismatch plus a new test mock missing IBrowser.major. The latter test was removed in favor of the executed Jest suite. `./node_modules/.bin/tsc --project packages/drive-store/tsconfig.json --noEmit --pretty false` exited 2 for the same crypto mismatch, existing drive-store missing exports/config, and the Jest mock missing IBrowser.major. Fixed the mock; project-wide checks remain limited by unrelated existing errors.

Final patch: both Drive parser copies now use meaningful File.type first and extension fallback without ChunkFileReader. JXL enum/extension mapping added. Shared image support gates HEIC family and JXL on Mac OS/iOS Safari 17+ using Version.isGreaterThanOrEqual.

Final verification: `./node_modules/.bin/jest --config packages/drive-store/jest.config.js --runInBand --coverage=false packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.test.ts packages/drive-store/store/_uploads/mimeTypeParser/imageSupport.test.ts` exited 0 (2 suites, 8 tests). `./node_modules/.bin/prettier --check packages/shared/lib/helpers/mimetype.ts packages/shared/lib/drive/constants.ts packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.ts packages/drive-store/store/_uploads/mimeTypeParser/mimeTypeParser.test.ts packages/drive-store/store/_uploads/mimeTypeParser/imageSupport.test.ts applications/drive/src/app/store/_uploads/mimeTypeParser/mimeTypeParser.ts` exited 0. `git diff --check` exited 0.
