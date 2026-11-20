# XAttr refactor checkpoint

Task complete: moved the implementation to `applications/drive/src/app/services/extendedAttributes.ts`, kept the previous module path as a reexport, added `DeepPartial`, and updated the upload call to pass `XAttrCreateParams`. Creation now omits zero remainders and absent digests, normalizes SHA1, and freezes its result. Parsing validates known fields and returns undefined for malformed or missing values.

Verification: focused extended-attribute Jest suite passed (5 tests); drive TypeScript check passed; ESLint and Prettier checks passed; `git diff --check` passed. No git history, index baseline, or harness configuration changes.
