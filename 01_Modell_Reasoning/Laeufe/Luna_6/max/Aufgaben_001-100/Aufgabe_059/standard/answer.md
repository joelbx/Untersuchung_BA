Added the forward-ref [Dialog abstraction](</app/packages/components/components/dialog/Dialog.tsx:10>) and exported it publicly. It forwards attributes and the host ref, uses native `<dialog>` when supported, and falls back to an accessible `div` when dialog support is limited.

[ModalTwo](</app/packages/components/components/modalTwo/Modal.tsx:149>) now uses Dialog with `open` and modal accessibility attributes, keeping its children accessible in JSDOM.

Validation passed: type-check, ESLint, diff check, and the existing ModalTwo suite (8 tests).