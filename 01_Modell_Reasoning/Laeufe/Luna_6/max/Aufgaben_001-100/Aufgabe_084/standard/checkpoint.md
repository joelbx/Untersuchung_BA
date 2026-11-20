# Checkpoint

Implemented `removeTechnicalFields<E extends SomeEntity>(entity: E): void` in `src/api/common/utils/EntityUtils.ts`. It mutates the full entity tree, removes keys with `_finalEncrypted`, `_defaultEncrypted`, and `_errors` prefixes, traverses arrays and nested objects, and guards against cycles.

Verification:
- `npm run types` passed.
- `npm run fasttest` passed: all 8,676 assertions passed.
- `git diff --check` passed.
