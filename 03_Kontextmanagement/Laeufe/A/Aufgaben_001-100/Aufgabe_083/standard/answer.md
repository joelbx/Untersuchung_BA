Refactored the Drive XAttr helpers to use `XAttrCreateParams`, added `DeepPartial`, and updated the upload call site. Creation now returns an immutable structure with correct chunk boundaries; parsing handles malformed or partial data and normalizes SHA1 digests.

Verification passed: 5 focused tests, the Drive TypeScript check, and `git diff --check`.