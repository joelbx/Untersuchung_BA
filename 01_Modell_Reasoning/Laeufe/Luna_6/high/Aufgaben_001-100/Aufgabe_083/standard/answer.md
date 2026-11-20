Updated the XAttr helpers to use `XAttrCreateParams`, added the recursive `DeepPartial` type, and made parsing resilient to invalid or partial input. Creation now omits zero remainders and absent digests, while digest keys are normalized to `SHA1`. Updated the upload call site and XAttr tests.

Verification passed: focused Jest suite (4 tests), Drive TypeScript check, Prettier check, and `git diff --check`.

Key files: [extendedAttributes.ts](/app/applications/drive/src/app/store/_links/extendedAttributes.ts), [DeepPartial.ts](/app/applications/drive/src/app/utils/type/DeepPartial.ts).