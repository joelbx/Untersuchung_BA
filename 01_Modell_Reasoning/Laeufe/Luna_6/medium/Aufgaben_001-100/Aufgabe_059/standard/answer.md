Implemented the Dialog abstraction and updated ModalTwo to use it. Dialog forwards props and its ref to either a native `<dialog>` or an accessible `<div>` fallback, depending on dialog support.

Verification passed: all 8 ModalTwo tests, the components TypeScript check, and `git diff --check`.