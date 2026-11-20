Implemented `removeTechnicalFields` in [EntityUtils.ts](/app/src/api/common/utils/EntityUtils.ts:222). It recursively removes the three technical field prefixes in place, including inside arrays and nested objects, and handles cyclic references.

Verification passed: `npm run types`, `npm run fasttest` (8,676 assertions), and `git diff --check`.