# Checkpoint

Implemented `components/dialog/Dialog.tsx` as a ref-forwarding abstraction that uses native `<dialog>` when `showModal` is available and an accessible `<div role="dialog">` fallback otherwise. Props and refs are forwarded in either branch. Exported Dialog from the components barrel and updated ModalTwo to use it with an open, modal dialog host.

Verification completed:
- `yarn workspace @proton/components test ModalTwo.test.tsx --runInBand` — passed (8 tests).
- `yarn workspace @proton/components check-types --pretty false` — passed.
- `git diff --check` — passed.
