# Checkpoint

Task: Resolve the JSDOM `<dialog>` incompatibility by adding a substitutable Dialog abstraction and updating ModalTwo to use it.

Initial inspection found that ModalTwo rendered a closed native `<dialog>` and there was no standalone Dialog abstraction. Added `components/dialog/Dialog.tsx` with a forward ref, native support detection, a `div` fallback with dialog semantics, and public exports. ModalTwo now uses that abstraction with `open` and modal accessibility attributes.

Validation completed: `yarn workspace @proton/components check-types` passed; the existing `ModalTwo.test.tsx` suite passed (8 tests); ESLint passed for the changed TypeScript files; `git diff --check` passed.
