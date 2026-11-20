Task: Implement removeTechnicalFields in src/api/common/utils/EntityUtils.ts.
Status: Complete. Added recursive, in-place removal for _finalEncrypted, _defaultEncrypted, and _errors prefixes across the entity, nested objects, and arrays. Added regression tests for unchanged clean entities and cleanup of cloned entities.
Verification: test TypeScript check passed; existing app test suite passed (8,690 assertions); Prettier and ESLint passed for changed files; git diff --check passed.
Constraints observed: Git history, index baseline, and harness configuration unchanged.
