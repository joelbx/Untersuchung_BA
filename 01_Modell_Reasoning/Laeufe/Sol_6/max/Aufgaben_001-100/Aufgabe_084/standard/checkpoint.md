Task: Implement `removeTechnicalFields` in `src/api/common/utils/EntityUtils.ts` for recursive removal of `_finalEncrypted`, `_defaultEncrypted`, and `_errors` prefixed properties from cloned entities.

Status: Complete. Added recursive `removeTechnicalFields` with cycle protection and EntityUtils tests for unchanged entities and root/nested cleanup. Full unit suite passed (8,688 assertions); source and test TypeScript checks, ESLint, Prettier, and `git diff --check` passed.
