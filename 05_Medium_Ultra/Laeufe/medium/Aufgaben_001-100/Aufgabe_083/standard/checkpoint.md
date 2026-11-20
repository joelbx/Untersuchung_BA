Task: Refactor Drive extended-attribute helpers to object parameter and strict, resilient parsing.
Status: Complete. Added public DeepPartial, XAttrCreateParams, and MaybeExtendedAttributes. Updated creation/encryption call sites, immutable attributes, exact chunk partitioning, canonical digests, and resilient parsing. Added focused regression cases.
Validation: Drive extendedAttributes Jest suite passed (4 tests); Drive strict TypeScript check passed; Prettier check and git diff --check passed.
Note: In this checkout the implementation is app/store/_links/extendedAttributes.ts, rather than the issue's app/services path. Encryption retains its required key arguments per the detailed interface.
