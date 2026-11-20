# Checkpoint

Implemented the Dialog abstraction at `packages/components/components/dialog/Dialog.tsx`. It forwards host props and refs, uses native `<dialog>` where `showModal()` is supported, and falls back to a `div` with dialog semantics in limited DOM environments. Exported it from the components barrel and replaced ModalTwo's direct native dialog with the abstraction, including its open and modal accessibility state.

Verification: `yarn workspace @proton/components test --runTestsByPath components/modalTwo/ModalTwo.test.tsx --coverage=false` passed (8 tests); `yarn workspace @proton/components check-types --pretty false` passed; `git diff --check` passed.
