Refactored Drive XAttr creation to use `XAttrCreateParams` and added the public `DeepPartial` type. Created file attributes are immutable, omit an exact zero-size remainder block, and include canonical digest keys when supplied. Parsing now returns unset fields for invalid or partial input without throwing.

The implementation is at [extendedAttributes.ts](/app/applications/drive/src/app/services/extendedAttributes.ts); the existing import path remains available. Encryption takes the options object alongside its required key references.

The focused tests (4), Drive TypeScript check, ESLint, Prettier, and `git diff --check` all passed.