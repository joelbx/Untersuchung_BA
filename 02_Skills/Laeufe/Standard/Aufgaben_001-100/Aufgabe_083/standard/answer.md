Refactored Drive’s extended-attribute helpers to use `XAttrCreateParams` and added strict `DeepPartial` based types. File creation now omits a zero chunk remainder and absent digests; parsing returns a neutral structure for malformed or partial data. I updated the upload call site and tests.

The focused tests, TypeScript check, ESLint, Prettier, and `git diff --check` all passed.