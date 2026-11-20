Implemented `removeTechnicalFields<E extends SomeEntity>(entity: E): void` in [EntityUtils.ts](/app/src/api/common/utils/EntityUtils.ts:138). It removes the specified technical fields recursively from nested objects and arrays, while leaving other fields intact.

Verification passed: `npm run types`, `npm run fasttest` (8,676 assertions), and `git diff --check`.