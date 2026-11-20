Refactored the Drive extended-attribute helpers to use `XAttrCreateParams`, added `DeepPartial` and explicit public types, and updated the upload caller. Creation now omits a zero-sized final block; parsing safely handles malformed nested data.

Verification passed: TypeScript check, all 327 Drive tests, and `git diff --check`. The test run emitted V8 warnings from the bundled OpenPGP dependency.