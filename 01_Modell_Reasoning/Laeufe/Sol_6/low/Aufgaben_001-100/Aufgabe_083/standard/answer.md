Refactored the Drive XAttr helpers to use `XAttrCreateParams`, added `DeepPartial` and `MaybeExtendedAttributes`, and updated the upload caller. Parsing now handles invalid or partial data without throwing, while creation omits a zero chunk remainder and normalizes digest keys.

Verification passed: 5 XAttr tests, the Drive TypeScript check, and `git diff --check`.