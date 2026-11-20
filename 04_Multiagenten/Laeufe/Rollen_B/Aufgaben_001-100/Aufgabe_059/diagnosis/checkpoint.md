# Fault localization progress

Inspected `modalTwo/Modal.tsx`, its existing tests, focus trap, CSS, and exports. No project source or tests modified.

Likely fault: `ModalTwo` renders a native `<dialog>` directly at lines 148–164 without `open` or `showModal()`. JSDOM creates the element but lacks native dialog operations; Testing Library treats descendants as hidden while `open` is absent. Local JSDOM probe: `querySelector('button')` finds a child; `queryByRole('button', { name: 'Hello' })` does not until the dialog receives `open`.

Likely change sites: new `components/dialog/Dialog.tsx` as a `forwardRef` host abstraction; `modalTwo/Modal.tsx` to use it; public export wiring if the interface is intended for package consumers. The abstraction needs environment substitution/fallback and must pass all attributes, children, and ref through. ModalTwo's focus trap/hotkeys depend on the host ref. Existing `ModalTwo.test.tsx` only checks test IDs and never exercises role visibility.

Uncertainty: A default wrapper around an unchanged closed `<dialog>` will not make role queries pass. The fix must either supply an open native host or select a fallback host in JSDOM. Avoid selecting native solely because `HTMLDialogElement` exists, as this JSDOM provides its constructor without `showModal`/`close`.
